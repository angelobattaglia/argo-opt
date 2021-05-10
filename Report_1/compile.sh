#!/bin/bash

echo "
###
Autocompiling LaTeX script by Angelo Battaglia
###
"

rm *.pdf

# If you want a Shell based build system, just uncomment below

#echo "
###################
###################
#Using biber for the references
###################
###################
#````
#"
#biber Report_1

#echo "
###################
###################
#Compiling LaTeX using pdflatex Report_1.tex
###################
###################
#"
#pdflatex Report_1.tex

make