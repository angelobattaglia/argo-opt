#/usr/bin/bash

echo "Compiling LaTeX using pdflatex Report_1.tex"
pdflatex Report_1.tex
echo "Using biber for the references"
biber Report_1

rm Report_1.aux Report_1..bbl Report_1.bbl Report_1.bcf Report_1.blg Report_1..blg Report_1.fdb_latexmk Report_1.fls Report_1.log Report_1.run.xml Report_1.tex.bbl Report_1.tex.blg uni.bib.bbl uni.bib.blg


