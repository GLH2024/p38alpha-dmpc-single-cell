from __future__ import annotations
import ast
import base64
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []
notebooks = sorted((ROOT / "notebooks").glob("*.ipynb"))
image_count = 0
cell_ids = set()

for path in notebooks:
    relative = path.relative_to(ROOT).as_posix()
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{relative}: invalid JSON: {exc}")
        continue
    cells = notebook.get("cells", [])
    if not cells or cells[0].get("cell_type") != "markdown":
        errors.append(f"{relative}: missing title cell")
    language = notebook.get("metadata", {}).get("kernelspec", {}).get("language", "").lower()
    for index, cell in enumerate(cells, 1):
        cell_id = cell.get("id")
        if not cell_id:
            errors.append(f"{relative} cell {index}: missing cell id")
        elif (relative, cell_id) in cell_ids:
            errors.append(f"{relative} cell {index}: duplicate cell id {cell_id}")
        else:
            cell_ids.add((relative, cell_id))
        source = "".join(cell.get("source", []))
        if cell.get("cell_type") == "code" and language == "python":
            try:
                ast.parse(source)
            except SyntaxError as exc:
                errors.append(f"{relative} cell {index}: Python syntax: {exc}")
        for output in cell.get("outputs", []):
            for mime, payload in output.get("data", {}).items():
                if mime.startswith("image/"):
                    payload = "".join(payload) if isinstance(payload, list) else payload
                    try:
                        base64.b64decode(payload, validate=True)
                        image_count += 1
                    except Exception as exc:
                        errors.append(f"{relative} cell {index}: invalid embedded image: {exc}")

if errors:
    raise SystemExit("\n".join(errors))
print(f"Validated {len(notebooks)} notebooks, {sum(len(json.loads(p.read_text(encoding='utf-8'))['cells']) for p in notebooks)} cells, and {image_count} embedded images.")
