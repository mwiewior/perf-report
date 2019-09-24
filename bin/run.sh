#!/bin/bash -x
#Rscript -e "library(knitr); knit('performance.Rmd')"

docker run --rm -it -v $PWD:/tmp -v $1:/data biodatageeks/perf-report-generator:0.1 sh -c "cd /tmp && Rscript -e \"library(knitr); rmarkdown::render('performance.Rmd')\""
