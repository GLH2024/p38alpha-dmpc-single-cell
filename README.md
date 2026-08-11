# p38 single-cell analysis

Publication-oriented, executable notebooks for the WT versus p38a-dMPC single-cell analysis. The original notebooks were not modified. This repository preserves their computational order and embedded figure outputs while removing empty/duplicate fragments, correcting kernels, centralizing paths and thread limits, and consolidating the final cluster naming/palette into one table.

## Run order

1. `01_qc_wt.ipynb` and `02_qc_p38a_dmpc.ipynb`
2. `03_harmony_integration.ipynb`
3. `04_singler_reference_annotation.ipynb`
4. `05_iterative_subclustering.ipynb`
5. `06_final_cell_type_annotation.ipynb`
6. `07_marker_validation.ipynb`
7. `08`-`14`: velocity, enrichment, and manuscript panels

The notebooks under `notebooks/exploratory/` retain earlier annotation stages for provenance but are not part of the main run order.

## Configuration

Set paths without editing notebook code:

```bash
export P38_PROJECT_ROOT=/data3/Group8/gonglihao/项目/p38
export P38_LEGACY_ROOT=/data3/Group8/gonglihao
export P38_OUTPUT_ROOT=/data3/Group8/gonglihao/codex/p38_publication_outputs
export P38_WORKERS=8
```

On SGE, `NSLOTS` overrides `P38_WORKERS`. R and Python thread variables are set to the allocated value to prevent oversubscription. Start Jupyter from the repository root (preferred) or from `notebooks/`, then use **Restart Kernel and Run All**.

## Reproducibility notes

- Random seed: 1234 by default (`P38_RANDOM_SEED` for Python).
- Final cluster names and colors: `config/cell_types.csv`.
- Central paths: `config/paths.R` and `config/paths.py`.
- Figure provenance: `FIGURE_MAP.md`.
- Package lists: `environment/`.
- Static notebook and embedded-image checks: `python tools/validate_notebooks.py`.

Large `.rds`, `.h5ad`, Cell Ranger matrices, and regenerated results are intentionally excluded from Git. The embedded notebook images are retained to allow visual comparison with the manuscript composite.
