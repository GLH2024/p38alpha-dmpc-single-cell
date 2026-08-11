# Server input audit

Read-only check performed on `172.18.5.221` on 2026-08-11.

## Present

- `20250509-doublet-p38/1QC/2stsub.rds`
- `20250526p38-draw/sub/2stsub.rds`
- `20250604p38-afterYZ/anno.rds`
- `20250509-doublet-p38/2-anno/velocity/velocity_ready_full_with_detailed_index_check.h5ad`
- `20250526p38-draw/velocity/velocity_ready_full_with_detailed_index_check.h5ad`
- `20250526p38-draw/sub/dynamo/velocity_ready_full_with_detailed_index_check.h5ad`
- `20260126p38拟时序修图/monocle3_results_combined.rds`
- `20260103-p38/final_results/adata_wt_dynamo_quantified.h5ad`
- `20260103-p38/final_results/adata_ko_dynamo_quantified.h5ad`

All paths above are relative to `/data3/Group8/gonglihao/项目/p38`.

## Not found

- `WT_cellranger_output.loom`
- `KO_cellranger_output.loom`
- The old `/data3/Group8/gonglihao/20250507p38-up/...` Cell Ranger locations referenced by the initial QC notebooks.

Consequently, the publication repository can start from the retained RDS/H5AD intermediates. A complete rerun from raw Cell Ranger matrices through loom alignment requires restoring or relinking those raw inputs and setting the configured roots accordingly.
