#!/bin/bash -x
sudo pip install pyNmonAnalyzer

echo -e "
knitr\n 
purrr\n
tidyr\n
ggplot2" | xargs -I {} sudo Rscript -e "install.packages('{}', dependencies = TRUE, repos = 'http://cran.us.r-project.org')"
