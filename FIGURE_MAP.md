# Figure-to-code map

The mapping was checked against the composite figure supplied with the source code. Original cell indices are retained in each cell's `metadata.provenance`; the curated cell number below accounts for the two new header/config cells.

| Panel | Notebook | Curated cell | Content |
|---|---|---:|---|
| Fig. 2A | `notebooks/06_final_cell_type_annotation.ipynb` | 3 | Final annotated UMAP; final palette loaded from config/cell_types.csv |
| Fig. 2B | `notebooks/06_final_cell_type_annotation.ipynb` | 7 | Cell-type marker dot plot |
| Fig. 2C | `notebooks/06_final_cell_type_annotation.ipynb` | 10 | WT versus p38a-dMPC cell proportions |
| Fig. 2D | `notebooks/08_rna_velocity.ipynb` | 2 | WT/p38a-dMPC vector-field panels; trajectory companion in notebook 13 |
| Fig. 4A | `notebooks/06_final_cell_type_annotation.ipynb` | 13 | Faceted differential-expression plot |
| Fig. 4D | `notebooks/06_final_cell_type_annotation.ipynb` | 14 | Nedd4 and Csf1r feature plots |
| Fig. 6D | `notebooks/10_fig6d_go_bubble.ipynb` | 3 | GO enrichment bubble plot |
| Fig. 6E | `notebooks/11_fig6e_gsea.ipynb` | 2 | GSEA running-score plot |
| Fig. 6F | `notebooks/14_fig_s3e_dynamics_metrics.ipynb` | 5 | Differential RNA-velocity bar plot |
| Fig. S3A | `notebooks/07_marker_validation.ipynb` | 4 | Marker FeaturePlot/violin/dot-plot series |
| Fig. S3B | `notebooks/06_final_cell_type_annotation.ipynb` | 7 | Marker-expression heatmap/dot-plot code block |
| Fig. S3C | `notebooks/12_fig_s3c_cell_proportions.ipynb` | 4 | Cell-proportion log2 fold-change plot |
| Fig. S3D | `notebooks/13_fig_s3d_pseudotime.ipynb` | 9 | Cell-type pseudotime ridge plot |
| Fig. S3E | `notebooks/14_fig_s3e_dynamics_metrics.ipynb` | 3 | Six dynamical-metric comparisons |

> Some manuscript panels were assembled from multiple notebook outputs. The embedded outputs are visual references; rerun from the top after setting paths to regenerate them.
