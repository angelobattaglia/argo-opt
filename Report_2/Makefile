# Just type 'make' and you'll have the .pdf
all: Report_2.pdf

MAIN = Report_2
TEX_SOURCES = Makefile \
              $(MAIN).tex \
              uni.bib
FIGURES := $(shell find images/* -type f)
SHELL=/bin/bash

$(MAIN).pdf: $(TEX_SOURCES) $(FIGURES)
	pdflatex $(MAIN)
	#makeindex $(MAIN)
	biber $(MAIN)
	pdflatex $(MAIN)
	pdflatex $(MAIN)

clean: 
	rm -f $(MAIN).{pdf,log,blg,bb,aux,out,toc,idx,bcf,run.xml,ind,ilg,fls,fdb_latexmk,bbl}

clean-pdf: 
	rm -f $(MAIN).{log,blg,bb,aux,out,toc,idx,bcf,run.xml,ind,ilg,fls,fdb_latexmk,bbl}

.PHONY: clean all
