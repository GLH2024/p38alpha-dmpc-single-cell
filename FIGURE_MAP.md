# Figure-to-code map

The mapping was checked against the supplied manuscript composite. Cell numbers are 1-based notebook cell positions.

| Panel | Notebook | Cell | Output / role |
|---|---|---:|---|
| Fig. 2A | `notebooks/06_final_cell_type_annotation.ipynb` | 3 | Final annotated UMAP |
| Fig. 2B | `notebooks/06_final_cell_type_annotation.ipynb` | 7 | Marker dot plot |
| Fig. 2C | `notebooks/06_final_cell_type_annotation.ipynb` | 10 | WT versus p38a-dMPC proportions |
| Fig. 2D | `notebooks/08_rna_velocity.ipynb` | 2 | Vector-field panels; pseudotime companion in notebook 13 |
| Fig. 4A | `notebooks/06_final_cell_type_annotation.ipynb` | 13 | Faceted differential-expression plot |
| Fig. 4B | `notebooks/17_fig4b_nedd4_pseudotime.ipynb` | 6 | Monocle3 pseudotime–*Nedd4* GAM plot |
| Fig. 4C | — | — | Western blot; experimental panel, no single-cell code |
| Fig. 4D | `notebooks/06_final_cell_type_annotation.ipynb` | 14 | *Nedd4* and *Csf1r* feature plots |
| Fig. 6D | `notebooks/10_fig6d_go_bubble.ipynb` | 3 | GO enrichment bubble plot |
| Fig. 6E | `notebooks/11_fig6e_gsea.ipynb` | 2 | GSEA running-score plot |
| Fig. 6F | `notebooks/14_fig_s3e_dynamics_metrics.ipynb` | 5 | Differential velocity bar plot |
| Fig. S3A | `notebooks/07_marker_validation.ipynb` | 4 | Marker feature/violin/dot plots |
| Fig. S3B | `notebooks/06_final_cell_type_annotation.ipynb` | 7 | Marker-expression heatmap/dot-plot block |
| Fig. S3C | `notebooks/12_fig_s3c_cell_proportions.ipynb` | 4 | Cell-proportion log2 fold-change |
| Fig. S3D | `notebooks/13_fig_s3d_pseudotime.ipynb` | 9 | Cell-type pseudotime ridges |
| Fig. S3E | `notebooks/14_fig_s3e_dynamics_metrics.ipynb` | 3 | Six dynamical metrics |

`notebooks/16_figure2_4_exports.ipynb` contains the later publication export code for Figure 2/4 panels. `notebooks/18_full_dynamo_quantification.ipynb` generates the Dynamo quantities consumed by velocity summaries. Some manuscript panels were assembled from multiple exported plots; embedded notebook images are visual references, not substitutes for rerunning the analysis.
