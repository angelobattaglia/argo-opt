#!/bin/bash
echo "
###
Autocompiling LaTeX script by Angelo Battaglia
###
"

echo "
##################
##################
Using biber for the references
##################
##################
````
"
biber Report_1

echo "
##################
##################
Compiling LaTeX using pdflatex Report_1.tex
##################
##################
"
pdflatex Report_1.tex

