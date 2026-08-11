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
8. `15a`-`15b`: upstream Seurat/loom export and velocity-ready H5AD construction
9. `16`-`19`: formal figure exports, DEG summary, and GSVA
10. `20`-`22`: Dynamo quantification, all-cell-type Monocle3, and Tcf4 velocity
11. `23`-`25`: pDC and DC regulator supplementary analyses

The notebooks under `notebooks/exploratory/` retain earlier annotation stages for provenance but are not part of the main run order.

## Configuration

Set paths without editing notebook code:

```bash
export P38_PROJECT_ROOT=/data3/Group8/gonglihao/项目/p38
export P38_LEGACY_ROOT=/data3/Group8/gonglihao/项目/p38
export P38_OUTPUT_ROOT=/data3/Group8/gonglihao/codex/p38_publication_outputs
export P38_WORKERS=8
export P38_TARGET_CELLTYPE='4 CD115+ CDP'
```

On SGE, `NSLOTS` overrides `P38_WORKERS`. R and Python thread variables are set to the allocated value to prevent oversubscription. Start Jupyter from the repository root (preferred) or from `notebooks/`, then use **Restart Kernel and Run All**.

The project was moved under `项目/p38`, so both default roots point there. The original WT/KO Cell Ranger matrices and loom files referenced by the oldest QC/velocity notebooks were not found during the server audit; downstream RDS/H5AD inputs are present. See `validation/INPUT_AUDIT.md`.

## Reproducibility notes

- Random seed: 1234 by default (`P38_RANDOM_SEED` for Python).
- Final cluster names and colors: `config/cell_types.csv`.
- Central paths: `config/paths.R` and `config/paths.py`.
- Figure provenance: `FIGURE_MAP.md`.
- Full server-code disposition: `REMOTE_AUDIT.md`.
- Package lists: `environment/`.
- Static notebook and embedded-image checks: `python tools/validate_notebooks.py`.

Large `.rds`, `.h5ad`, loom/Cell Ranger matrices, and regenerated results are intentionally excluded from Git. The embedded notebook images are retained to allow visual comparison with the manuscript composite.
