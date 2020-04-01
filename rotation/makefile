TARGET=rotation
#EPS=$(shell ls *.eps)
TEX=platex
DVIPDF=dvipdfmx

.SUFFIXES: .tex .dvi .pdf

all:$(TARGET).pdf
	open $(TARGET).pdf

$(TARGET).pdf: $(TARGET).dvi $(EPS)

$(TARGET).dvi: $(TARGET).tex $(EPS)

.dvi.pdf:
	$(DVIPDF) $(TARGET).dvi

.tex.dvi:
	$(TEX) $<
	$(TEX) $<

tar:
	tar cvzf $(TARGET).tar.gz $(TARGET).* *.eps

clean:
	rm -f $(TARGET).dvi $(TARGET).aux $(TARGET).log $(TARGET).toc
	rm -f $(TARGET).pdf $(TARGET).tar.gz 
	rm -f *.pbm *.bmc
