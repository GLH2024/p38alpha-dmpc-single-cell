p38_project_root <- Sys.getenv("P38_PROJECT_ROOT", "/data3/Group8/gonglihao/项目/p38")
p38_output_root <- Sys.getenv("P38_OUTPUT_ROOT", file.path(p38_project_root, "p38_publication_outputs"))
p38_upstream_root <- Sys.getenv("P38_UPSTREAM_ROOT", "/data3/Group8/gonglihao/20250507p38-up")
p38_workers <- as.integer(Sys.getenv("NSLOTS", Sys.getenv("P38_WORKERS", "4")))
if (is.na(p38_workers) || p38_workers < 1L) p38_workers <- 1L
Sys.setenv(OMP_NUM_THREADS=p38_workers, OPENBLAS_NUM_THREADS=p38_workers, MKL_NUM_THREADS=p38_workers)
p38_path <- function(...) file.path(p38_project_root, ...)
legacy_path <- p38_path
upstream_path <- function(...) file.path(p38_upstream_root, ...)
output_path <- function(...) {
  path <- file.path(p38_output_root, ...)
  dir.create(dirname(path), recursive=TRUE, showWarnings=FALSE)
  path
}
