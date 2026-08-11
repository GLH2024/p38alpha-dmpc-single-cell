from __future__ import annotations
import os
from pathlib import Path

P38_PROJECT_ROOT = Path(os.getenv("P38_PROJECT_ROOT", "/data3/Group8/gonglihao/项目/p38"))
P38_LEGACY_ROOT = Path(os.getenv("P38_LEGACY_ROOT", "/data3/Group8/gonglihao/项目/p38"))
P38_OUTPUT_ROOT = Path(os.getenv("P38_OUTPUT_ROOT", str(P38_LEGACY_ROOT / "p38_publication_outputs")))
P38_THREADS = int(os.getenv("NSLOTS", os.getenv("P38_THREADS", "4")))
RANDOM_SEED = int(os.getenv("P38_RANDOM_SEED", "1234"))
for variable in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[variable] = str(P38_THREADS)

def p38_path(*parts: str) -> str:
    return str(P38_PROJECT_ROOT.joinpath(*parts))

def legacy_path(*parts: str) -> str:
    return str(P38_LEGACY_ROOT.joinpath(*parts))

def output_path(*parts: str) -> str:
    path = P38_OUTPUT_ROOT.joinpath(*parts)
    path.parent.mkdir(parents=True, exist_ok=True)
    return str(path)
