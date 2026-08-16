# Reproducible environments

Versions below were inspected on `172.18.5.221` on 2026-08-16. Use the absolute executables in batch jobs and set `OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, `MKL_NUM_THREADS` (and Python `NUMEXPR_NUM_THREADS`) to `NSLOTS`.

| Purpose | Conda environment | Runtime / kernel | Key versions |
|---|---|---|---|
| R, Seurat, Monocle3 | `/home/gonglihao/miniconda3/envs/42` | R 4.4.2; `42r` | Seurat 5.1.0, SeuratObject 5.0.2, monocle3 1.3.1 |
| General Python | `/home/gonglihao/miniconda3/envs/310` | Python 3.10.16; `310` | scanpy 1.10.4, anndata 0.11.3, NumPy 1.23.5 |
| Dynamo | `/home/gonglihao/miniconda3/envs/dynamo_env` | Python 3.8.20; `dynamo` | dynamo-release 1.4.1, scanpy 1.9.6, anndata 0.9.2 |
| velocyto upstream | `/home/gonglihao/miniconda3/envs/velocyto_env` | Python 3.12.10 | velocyto 0.17.17, loompy 2.0.16 |
| Cell Ranger upstream | `/home/gonglihao/miniconda3/envs/cellranger_env` | executable not present in current env | exact Cell Ranger version not recoverable from this environment |
| CellChat | `/home/gonglihao/miniconda3/envs/cellchat_env` | outside scope | not required for the mapped panels |

Important: although `dynamo-release 1.3.2` metadata exists in `310`, importing it currently fails with Matplotlib 3.10 (`register_cmap` compatibility). The notebooks importing `dynamo` therefore point to `dynamo_env`, not `310`.

`ggplot2` resolves to runtime version 4.0.1 in R `42` because the user library overrides the conda package record. The version manifests record runtime versions, which are the versions that actually execute the notebooks.
