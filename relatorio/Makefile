# Makefile for latex project

plots=$(patsubst plots/%.gpi,images/%.eps,$(wildcard plots/*.gpi))

# Creates pdf output file
all: $(plots) refs
	pdflatex --shell-escape main.tex

# Create .dvi file
dvi: refs
	latex main

# Creates all the cross references
refs: $(plots)
	latex main
	# Uncomment to enable bibtex:
	#bibtex main
	#latex main

# gnuplot automatic rules
images/%.eps: plots/%.gpi plots/%.dat
	gnuplot $<

# Deletes all temporary files
clean:
	rm -rf *.aux *.bbl *.blg *.idx *.lof *.log *.lol *.lot *.toc *.dvi \
		*.pdf plots/*.eps plots/*.pdf

.PHONY: all dvi spell refs clean

