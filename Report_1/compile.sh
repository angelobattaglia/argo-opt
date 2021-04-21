#!/usr/bin/bash

echo "
##################
##################
Compiling LaTeX using pdflatex Report_1.tex
##################
##################
"
pdflatex Report_1.tex
echo "
##################
##################
Using biber for the references
##################
##################
````
"
biber Report_1

