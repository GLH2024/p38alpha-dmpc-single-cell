# Validation records

- `notebook_manifest.tsv`: notebook language, cell counts, embedded-image counts and SHA-256.
- `embedded_images.tsv`: every embedded image's notebook, cell, MIME type, byte size and SHA-256.
- `INPUT_AUDIT.md`: retained server intermediates and missing legacy raw-input paths.

Regenerate the first two files with `python tools/validate_notebooks.py` after any notebook edit.

The reconstructed Figure 4B analysis script was run under R environment `42` as SGE job `314205` on `all.q@icloud-mnode02.local` with two slots (`failed 0`, `exit_status 0`). The final `.ipynb` was then executed from its first cell through its plotting cell with Jupyter/`42r` as job `314208`; `qacct` reported `failed 0`, `exit_status 0`, wall time 91 s and max VMEM 9.595 GB. The tracked PDF/PNG and summary CSV under `figures/` are explicit publication-code deliverables; cell-level CSV output remains untracked because it is regenerable.
