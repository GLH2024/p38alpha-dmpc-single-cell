# p38α-dMPC single-cell analysis

Publication-oriented Jupyter notebooks for the WT versus p38α-dMPC single-cell RNA-seq study (GEO: [GSE341129](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE341129)). The original analysis directory is unchanged; this repository contains only the code required for Figures 2, 4, 6 and Figure S3 in the supplied manuscript composite.

## Workflow

Run notebooks from the repository root in filename order. The velocity branch is explicit and no longer begins from an unexplained H5AD:

```text
01-07 annotation
   └─> 08a Seurat export
        └─> 08b loom alignment -> velocity_ready_full_with_detailed_index_check.h5ad
             └─> 09 Dynamo fitting and metric quantification
                  ├─> 10 Fig. 2D velocity/trajectory plots
                  └─> 16 Fig. 6F / Fig. S3E dynamic metrics
```

| Notebooks | Purpose | Environment |
|---|---|---|
| `01`-`07` | QC, integration, annotation and marker validation | R `42` |
| `08a` | Export the final trajectory Seurat object | R `42` |
| `08b` | Align WT/KO velocyto loom layers and write velocity-ready H5AD | Python `310` |
| `09` | Fit Dynamo vector fields and save quantified WT/KO H5AD files | `dynamo_env` |
| `10` | Plot Fig. 2D from notebook 09 outputs | `dynamo_env` |
| `11`-`18` | Differential expression, enrichment and manuscript panels | kernel recorded per notebook |

Panel provenance is listed in [`FIGURE_MAP.md`](FIGURE_MAP.md). Figure 4C is a western blot and has no single-cell code.

## Paths and execution

```bash
export P38_PROJECT_ROOT=/data3/Group8/gonglihao/项目/p38
export P38_UPSTREAM_ROOT=/data3/Group8/gonglihao/20250507p38-up
export P38_OUTPUT_ROOT=/data3/Group8/gonglihao/codex/p38_publication_outputs
export P38_WORKERS=8
```

`P38_PROJECT_ROOT` contains retained RDS/H5AD intermediates. `P38_UPSTREAM_ROOT` contains Cell Ranger matrices and velocyto loom files and may be replaced with the corresponding GEO download location. On SGE, `NSLOTS` overrides `P38_WORKERS`. Start Jupyter from this repository root and use **Restart Kernel and Run All**.

## Data availability

Raw and processed data were deposited as [GSE341129](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE341129). As checked on 2026-08-16, the record was private and scheduled for release on 2030-07-23; reviewers require the GEO secure token supplied separately by the authors. Tokens and credentials must not be committed.

The canonical velocity input `20250526p38-draw/sub/2stsub.rds` and downstream H5AD are present on the analysis server. The two legacy loom paths referenced by notebook 08b are currently absent, so a clean raw-to-H5AD rerun requires restoring those GEO/velocyto files or regenerating them with `velocyto_env`. Large data files are intentionally excluded from Git.

## Environments and validation

Exact inspected package versions are in [`environment/`](environment/README.md). Notebooks importing Dynamo use `dynamo_env`; notebook 08b uses `310`; R notebooks use `42r`.

```bash
python scripts/validate_notebooks.py
```

The validator checks notebook JSON, cell IDs, Python syntax and embedded images. The reconstructed Fig. 4B notebook was executed under R `42` as SGE job `314208` (`failed 0`, `exit_status 0`). Velocity dependency smoke test `314272` used `dynamo_env 1.4.1` to verify the 18,113-cell input, the 8,176-cell trajectory subset (WT 4,694; p38α-dMPC 3,482), and the quantified H5AD outputs required by notebooks 10 and 16 (`failed 0`, `exit_status 0`). Embedded images are retained for visual comparison, but a clean raw-to-figure rerun remains necessary before claiming full independent reproducibility.

## Provenance

Curated cells retain `metadata.provenance` where source notebooks/cells were known. The server source directory and the original local code were read only. The repository structure follows the concise numbered-notebook approach of [irae_reproduction](https://github.com/chansigit/irae_reproduction).
