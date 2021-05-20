all: Report_2.pdf

Report_2.pdf : Report_2.tex
	pdflatex Report_2
	biber Report_2
	pdflatex Report_2
	pdflatex Report_2


# PROJECT = 'Report_1' 
# MAIN = Report_1
# TEX_SOURCES = Makefile \
              # $(MAIN).tex \
              # uni.bib \

# FIGURES := $(shell find images/* -type f)

# SHELL=/bin/bash
# DATE = $(shell date +"%d%b%Y")
# OPT = --interaction=nonstopmode

# all: $(MAIN).pdf

# final: final.pdf
	# $(MAKE) clean

# final.pdf: cover.pdf $(MAIN).pdf 
	# pdftk cover.pdf $(MAIN).pdf cat output final.pdf

# $(MAIN).pdf: $(TEX_SOURCES) $(FIGURES)
	# pdflatex $(MAIN)
	# makeindex $(MAIN)
	# bibtex $(MAIN)
	# pdflatex $(MAIN)
	# pdflatex $(MAIN)
	# @#latexmk -pdf -pvc -pdflatex="pdflatex $(OPT)" $(MAIN) 


# once: 
	# pdflatex $(MAIN)

# clean: 
	# -rm -f $(MAIN).{pdf,log,blg,bb,aux,out,toc,idx,bcf,run.xml,ind,ilg,fls,fdb_latexmk} final.pdf

# targz:
	# $(MAKE) clean
	# $(MAKE) all
	# $(MAKE) clean
	# tar czf $(PROJECT)_$(DATE).tgz $(TEX_SOURCES) $(FIGURES) cover.pdf

# zip:
	# $(MAKE) clean
	# $(MAKE) all
	# $(MAKE) clean
	# zip -q $(PROJECT)_$(DATE).zip $(TEX_SOURCES) $(FIGURES) cover.pdf
	
# .PHONY: clean all
