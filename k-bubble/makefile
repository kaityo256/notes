SRC=k-bubble.tex
DVI=$(SRC:.tex=.dvi)
PDF=$(SRC:.tex=.pdf)
JPG=$(shell ls *.jpg)
XBB=$(JPG:.jpg=.xbb)
STY=kotaibutsuri.sty
TEX=platex
DVIPDF=dvipdfmx

.SUFFIXES: .tex .dvi .pdf .jpg .xbb
.PHONY: submit

all:$(PDF) 
	open $(PDF)

$(DVI): $(SRC) $(STY) $(XBB)

$(PDF): $(DVI) 

.dvi.pdf:
	$(DVIPDF) $<

.jpg.xbb:
	extractbb $<

.tex.dvi: 
	$(TEX) $<
	$(TEX) $<

tar:
	tar cvzf $(TARGET).tar.gz $(TARGET).* $(EPS)

submit:
	mkdir -p submit
	cp *.pdf *.tex *.jpg *.xbb makefile *.sty submit
	zip -r watanabe.zip submit

clean:
	rm -f $(DVI) *.aux *.log *.toc $(PDF) *.pbm *.bmc $(XBB)
