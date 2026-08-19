DoubletRemovalParameters <- function(seu, PCs=1:30, use.SCT=FALSE, num.cores=1, quietly=TRUE) {
  tictoc::tic("sweep parameters")
  if (quietly) {
    invisible(capture.output(sweep.res.list <- DoubletFinder::paramSweep(seu, PCs=PCs, sct=use.SCT, num.cores=num.cores)))
    invisible(capture.output(sweep.stats <- DoubletFinder::summarizeSweep(sweep.res.list, GT=FALSE)))
    ff <- tempfile(fileext=".png"); png(ff)
    invisible(capture.output(bcmvn <- DoubletFinder::find.pK(sweep.stats)))
    dev.off(); unlink(ff)
  } else {
    sweep.res.list <- DoubletFinder::paramSweep(seu, PCs=PCs, sct=use.SCT, num.cores=num.cores)
    sweep.stats <- DoubletFinder::summarizeSweep(sweep.res.list, GT=FALSE)
    ff <- tempfile(fileext=".png"); png(ff); bcmvn <- DoubletFinder::find.pK(sweep.stats); dev.off(); unlink(ff)
  }
  tictoc::toc()
  max_metric <- max(bcmvn$BCmetric, na.rm=TRUE)
  list(pK=as.numeric(as.character(bcmvn[bcmvn$BCmetric == max_metric, ]$pK)), bcmvn=bcmvn)
}

bcmvnPlot <- function(bcmvn, maxpos=0.08) {
  data <- data.frame(pK=as.numeric(as.character(bcmvn$pK)), BCmvn=as.numeric(as.character(bcmvn$BCmetric)))
  ggplot2::ggplot(data, ggplot2::aes(pK, BCmvn)) + ggplot2::geom_point(color="#20639B") +
    ggplot2::geom_line(color="#3CAEA3") + ggplot2::geom_vline(xintercept=maxpos, linetype="dashed", color="red", linewidth=0.5)
}
