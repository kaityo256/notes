TARGET=prob
EPS=$(shell ls *.eps)
TEX=platex
DVIPDF=dvipdfmx

.SUFFIXES: .tex .dvi .pdf

all:$(TARGET).pdf
	open $(TARGET).pdf

$(TARGET).dvi: $(TARGET).tex $(EPS)
$(TARGET).pdf: $(TARGET).dvi

.tex.dvi:
	$(TEX) $<
	$(TEX) $<

tar:
	tar cvzf $(TARGET).tar.gz $(TARGET).* $(EPS)

.dvi.pdf:
	$(DVIPDF) $<

clean:
	rm -f $(TARGET).dvi $(TARGET).aux $(TARGET).log  $(TARGET).toc
	rm -f $(TARGET).pdf $(TARGET).tar.gz 
	rm -f *.pbm *.bmc
