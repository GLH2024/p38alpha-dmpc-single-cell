# Remote-code audit

Audited read-only on 2026-08-11: `/data3/Group8/gonglihao/项目/p38` (85 GB). The audit found 52 notebooks plus two helper scripts. Notebook comparison used both raw-file SHA-256 and code-only SHA-256 so saved-output differences were not mistaken for new analyses.

## Added to the publication repository

| Remote analysis | Curated notebook | Reason |
|---|---|---|
| Seurat/loom barcode alignment and H5AD construction | `15a_velocity_export_from_seurat.ipynb`, `15b_velocity_preprocessing.ipynb` | Missing upstream dependency for velocity/Dynamo |
| Formal UMAP, dot plot, proportions, volcano and feature exports | `16_figure2_4_exports.ipynb` | Direct source for Fig. 2/Fig. 4 export files |
| Per-cell-type DEG-count summary | `17_deg_summary.ipynb` | Later DEG summary not fully represented locally |
| GSVA heatmap and bubble plot | `18_gsva_heatmap.ipynb`, `19_gsva_bubble.ipynb` | Distinct pathway analysis |
| Dynamo vector-field quantification | `20_full_dynamo_quantification.ipynb` | Generates quantified WT/KO H5AD inputs used by later figures |
| Whole-cell-type Monocle3 comparisons | `21_monocle3_all_celltypes.ipynb` | Extends the manuscript-specific pseudotime notebook |
| Tcf4 velocity feature map | `22_tcf4_velocity_feature.ipynb` | Distinct Fig. 6-related driver visualization |
| pDC signature heatmap and half-violin plot | `23_pdc_signature_heatmap.ipynb`, `24_pdc_half_violin.ipynb` | Distinct supplementary pDC analyses |
| DC regulator/marker heatmap | `25_dc_regulator_heatmap.ipynb` | Distinct regulator panel |
| GO bubble alternatives | `exploratory/92_go_bubble_refinements.ipynb` | Retained as visually useful alternatives, outside the main run order |

The mixed R/Python velocity notebook was split into two notebooks so each has a valid kernel. The large Dynamo development notebook was reduced to the dependency-complete quantification path: load/joint embedding, condition-specific vector fields, core and advanced metrics, save quantified objects, and preview.

## Covered by existing notebooks

WT/KO QC, Harmony integration, SingleR, iterative subclustering, initial/intermediate/final annotation, marker validation, CDP velocity, CD115-positive CDP enrichment, Fig. 6 GO/GSEA, Fig. S3 proportions, pseudotime, and six Dynamo metrics all matched local source notebooks or their direct server copies.

## Consolidated instead of duplicated

- Five cell-type-specific DEG/GSEA/ORA notebooks (`0 Mzb1+ pDC`, `1 Iglc3+ pDC`, `2 DC progenitor`, `4 CD115+ CDP`, `7 CD115- CDP`) contain the same pipeline with changed target parameters. Notebook `09_cdp_deg_and_enrichment.ipynb` now reads `P38_TARGET_CELLTYPE`, covering all five without code duplication.
- `20260103-p38/CDP.ipynb` and `20250611-p38-draw/dynamo_processed_adata/CDP.ipynb` are byte-identical.
- Earlier velocity, Dynamo, volcano/alluvial, Monocle3 color-selection, pDC heatmap trials, three-/six-metric trials, and HarmonyIntegration notebooks were superseded by later or curated versions retained here.
- Incomplete enrichment fragments (`12pre-pDC.ipynb`, `7CD115-CDP.ipynb`) and the Excel-merging utility were not placed in the executable main pipeline because they depend on prior interactive state or generated result workbooks; their role is documented here.
- `inject_print_css.py` is a Jupyter display helper, not analysis code. The server-side `doublet_removal.R` functionality is already tracked in `R/doublet_removal.R`.
