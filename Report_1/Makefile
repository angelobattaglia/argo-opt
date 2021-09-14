# If you just type 'make' you'll get the .pdf
all: Report_1.pdf

MAIN = Report_1
TEX_RESOURCES = Makefile\
              $(MAIN).tex\
              uni.bib
SHELL = /bin/bash
FIGURES := $(shell find images/* -type f)

Report_1.pdf: $(TEX_RESOURCES) $(FIGURES)
	pdflatex $(MAIN)
	biber $(MAIN)
	pdflatex $(MAIN)
	pdflatex $(MAIN)

clean-pdf: 
	rm -f $(MAIN).{bbl,log,blg,bb,aux,out,toc,idx,bcf,run.xml,ind,ilg,fls,fdb_latexmk}

clean: 
	rm -f $(MAIN).{pdf,bbl,log,blg,bb,aux,out,toc,idx,bcf,run.xml,ind,ilg,fls,fdb_latexmk}

.PHONY: clean all
