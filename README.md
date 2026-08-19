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

| Notebooks | Purpose | Environment |
|---|---|---|
| `01`-`07` | QC, integration, annotation and marker validation | R `42` |
| `08a` | Export the final trajectory Seurat object | R `42` |
| `08b` | Align WT/KO velocyto loom layers and write velocity-ready H5AD | Python `310` |
| `09` | Fit Dynamo vector fields and save quantified WT/KO H5AD files | `dynamo_env` |
| `10` | Plot Fig. 2D from notebook 09 outputs | `dynamo_env` |
| `11`-`18` | Differential expression, enrichment and manuscript panels | kernel recorded per notebook |
