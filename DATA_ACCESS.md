# Data access and input audit

## GEO accession

- Accession: [GSE341129](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE341129)
- Status checked: 2026-08-16
- Current status: private; scheduled public release 2030-07-23
- Reviewer access: requires the GEO secure token supplied separately by the authors

Do not commit reviewer tokens, credentials or controlled links.

## Retained server intermediates

The following inputs were verified under `/data3/Group8/gonglihao/项目/p38`:

- `20250509-doublet-p38/1QC/2stsub.rds`
- `20250526p38-draw/sub/2stsub.rds`
- `20250604p38-afterYZ/anno.rds`
- `20250509-doublet-p38/2-anno/velocity/velocity_ready_full_with_detailed_index_check.h5ad`
- `20250526p38-draw/velocity/velocity_ready_full_with_detailed_index_check.h5ad`
- `20250526p38-draw/sub/dynamo/velocity_ready_full_with_detailed_index_check.h5ad`
- `20260126p38拟时序修图/monocle3_results_combined.rds`
- `20260103-p38/final_results/adata_wt_dynamo_quantified.h5ad`
- `20260103-p38/final_results/adata_ko_dynamo_quantified.h5ad`

The legacy WT/KO loom files and old `/data3/Group8/gonglihao/20250507p38-up/...` Cell Ranger locations were not found in the current audit. Consequently, the checked notebooks can rerun from retained intermediates, but a clean raw-to-figure rerun requires downloading/relinking the GEO files and setting the configured roots. This limitation should be resolved or documented for reviewers before submission.
