# p38α-dMPC single-cell analysis

Publication-oriented Jupyter notebooks for the WT versus p38α-dMPC single-cell RNA-seq study (GEO: [GSE341129](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE341129)). The original analysis directory is unchanged; this repository contains only the code required for Figures 2, 4, 6 and Figure S3 in the supplied manuscript composite.

## Workflow

Run notebooks from the repository root in filename order.

```text
01-07 annotation
   └─> 08a Seurat export
        └─> 08b loom alignment -> velocity_ready_full_with_detailed_index_check.h5ad
             └─> 09 Dynamo fitting and metric quantification
                  ├─> 10 Fig. 2D velocity/trajectory plots
                  └─> 16 Fig. 6F / Fig. S3E dynamic metrics
```

| Notebooks | Purpose | Environment | Key software versions |
|---|---|---|---|
| `01`-`07` | QC, integration, annotation and marker validation | R `42` (`42r`) | R 4.4.2; Seurat 5.1.0; SeuratObject 5.0.2; Harmony 1.2.3 |
| `08a` | Export the final trajectory Seurat object | R `42` (`42r`) | R 4.4.2; Seurat 5.1.0 |
| `08b` | Align WT/KO velocyto loom layers and write velocity-ready H5AD | Python `310` | Python 3.10.16; Scanpy 1.10.4; AnnData 0.11.3 |
| `09`-`10` | Fit Dynamo vector fields and plot Fig. 2D | `dynamo_env` | Python 3.8.20; Dynamo 1.4.1; Scanpy 1.9.6; AnnData 0.9.2 |
| `11`-`15`, `17`-`18` | Differential expression, enrichment and R-based manuscript panels | R `42` (`42r`) | R 4.4.2; monocle3 1.3.1; clusterProfiler 4.14.6; GseaVis 0.1.1 |
| `16` | Fig. 6F / Fig. S3E dynamic metrics | `dynamo_env` | Python 3.8.20; Dynamo 1.4.1; Scanpy 1.9.6; AnnData 0.9.2 |
