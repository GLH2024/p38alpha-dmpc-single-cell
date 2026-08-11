# Validation summary

Validation performed during curation:

- 16 notebooks parsed as valid notebook JSON.
- 133 R code cells parsed successfully with R 4.5.3.
- All Python code cells parsed successfully with Python AST.
- All 16 notebooks load the central configuration before analysis code.
- No hard-coded `/data3/Group8/gonglihao/` literal remains in notebook cells.
- 93 embedded images decoded successfully; every retained image has the same SHA-256 hash as its source-notebook image.
- Original cell order is retained through per-cell provenance metadata. Removed cells were empty, exact duplicates, short fragments already present in an earlier complete cell, or superseded palette trials.

This is a static and structural validation. A complete numerical rerun requires the server-side `.rds`, `.h5ad`, Cell Ranger matrices, and package environments documented in the repository.
