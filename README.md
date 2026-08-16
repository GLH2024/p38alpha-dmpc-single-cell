# p38 single-cell analysis

Publication-oriented Jupyter notebooks for the WT versus p38a-dMPC single-cell figures. The original analysis directory is unchanged; this repository is a curated copy limited to the panels in Figures 2, 4, 6 and Figure S3 shown in the supplied composite.

The layout follows the concise, numbered-notebook style of [irae_reproduction](https://github.com/chansigit/irae_reproduction), while retaining `.ipynb` outputs for panel-by-panel visual checking.

## Scope and run order

1. `01`–`07`: QC, integration, subclustering, final annotation and marker validation.
2. `08`: RNA velocity / trajectory visualization.
3. `09`–`14`: CDP differential expression, enrichment and manuscript panels.
4. `15a`–`15b`: Seurat export and velocity-ready H5AD construction.
5. `16`: final Figure 2/4 exports.
6. `17`: reconstructed Monocle3 pseudotime–*Nedd4* panel.
7. `18`: full Dynamo quantification supporting velocity metrics.

The exact panel-to-cell mapping is in [`FIGURE_MAP.md`](FIGURE_MAP.md). Figure 4C is a western blot and therefore has no single-cell analysis notebook.

## Data access

Raw and processed sequencing data were deposited as [GSE341129](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE341129). As checked on 2026-08-16, the GEO record is private and scheduled for release on 2030-07-23; peer reviewers therefore need the GEO secure reviewer token until public release. No token or credentials are stored here. See [`DATA_ACCESS.md`](DATA_ACCESS.md).

Large RDS, H5AD, loom and matrix files are excluded from Git. Server paths are centralized in `config/paths.R` and `config/paths.py`:

```bash
export P38_PROJECT_ROOT=/data3/Group8/gonglihao/项目/p38
export P38_LEGACY_ROOT=/data3/Group8/gonglihao/项目/p38
export P38_OUTPUT_ROOT=/data3/Group8/gonglihao/codex/p38_publication_outputs
export P38_WORKERS=8
```

Start Jupyter from the repository root and use **Restart Kernel and Run All**. Within a notebook, cells are ordered so variables are created before use; do not execute only the final plotting cell in a fresh kernel.

## Environments

- R/Seurat/Monocle3 notebooks: conda `42`, Jupyter kernel `R (42)`.
- General Python notebooks: conda `310`, kernel `Python (310)`.
- Dynamo notebooks: conda `dynamo_env`, kernel `Python (Dynamo)`.
- Upstream Cell Ranger and velocyto tooling: `cellranger_env` and `velocyto_env` respectively.
- CellChat is outside this figure-scoped repository.

Exact versions and known compatibility notes are in [`environment/README.md`](environment/README.md).

## Validation

Run:

```bash
python tools/validate_notebooks.py
```

The validator checks notebook JSON, Python syntax and embedded images and regenerates the manifests under `validation/`. The Figure 4B analysis script was validated as SGE job `314205`; the notebook itself was then checked with a separate **Run All** job recorded in `validation/README.md`. Static validation does not replace a clean-environment end-to-end rerun from GEO data before journal submission.
