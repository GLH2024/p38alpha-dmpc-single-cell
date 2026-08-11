from __future__ import annotations
import ast, base64, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
rows = []
images = []
errors = []
for path in sorted((ROOT / "notebooks").rglob("*.ipynb")):
    rel = path.relative_to(ROOT).as_posix()
    try:
        nb = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{rel}: invalid JSON: {exc}")
        continue
    language = nb.get("metadata", {}).get("kernelspec", {}).get("language", "")
    code_cells = [c for c in nb.get("cells", []) if c.get("cell_type") == "code"]
    if not nb.get("cells") or nb["cells"][0].get("cell_type") != "markdown":
        errors.append(f"{rel}: missing title cell")
    for index, cell in enumerate(nb.get("cells", [])):
        src = "".join(cell.get("source", [])) if isinstance(cell.get("source", []), list) else str(cell.get("source", ""))
        if cell.get("cell_type") == "code" and language == "python":
            try:
                ast.parse(src)
            except SyntaxError as exc:
                errors.append(f"{rel} cell {index}: Python syntax: {exc}")
        for output in cell.get("outputs", []):
            for mime, payload in output.get("data", {}).items():
                if mime.startswith("image/"):
                    payload = "".join(payload) if isinstance(payload, list) else payload
                    try:
                        raw = base64.b64decode(payload, validate=True)
                        images.append((rel, index, mime, len(raw), hashlib.sha256(raw).hexdigest()))
                    except Exception as exc:
                        errors.append(f"{rel} cell {index}: invalid embedded image: {exc}")
    rows.append((rel, language, len(nb.get("cells", [])), len(code_cells), sum(1 for x in images if x[0] == rel), hashlib.sha256(path.read_bytes()).hexdigest()))

validation = ROOT / "validation"
validation.mkdir(exist_ok=True)
(validation / "notebook_manifest.tsv").write_text("notebook\tlanguage\tcells\tcode_cells\tembedded_images\tsha256\n" + "".join("\t".join(map(str, row)) + "\n" for row in rows), encoding="utf-8")
(validation / "embedded_images.tsv").write_text("notebook\tcell\tmime\tbytes\tsha256\n" + "".join("\t".join(map(str, row)) + "\n" for row in images), encoding="utf-8")
if errors:
    raise SystemExit("\n".join(errors))
print(f"Validated {len(rows)} notebooks and {len(images)} embedded images.")
