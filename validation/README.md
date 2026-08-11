# Validation summary

Validation performed during curation:

- 29 notebooks parsed as valid notebook JSON.
- 200 R code cells parsed successfully with R 4.5.3.
- All Python code cells parsed successfully with Python AST.
- All 29 notebooks load the central configuration before analysis code.
- No hard-coded `/data3/Group8/gonglihao/` literal remains in notebook cells.
- 132 embedded images decoded successfully. All 93 original local images and all 39 newly retained remote images are SHA-256-identical to their source-notebook images.
- Original cell order is retained through per-cell provenance metadata. Removed cells were empty, exact duplicates, short fragments already present in an earlier complete cell, or superseded palette trials.
- Remote audit covered 52 notebooks under the 85 GB server project tree; exact copies, parameter-only copies, and superseded exploratory versions are documented in `REMOTE_AUDIT.md`.

This is a static and structural validation. A complete numerical rerun requires the server-side `.rds`, `.h5ad`, Cell Ranger matrices, and package environments documented in the repository.
