TARGET=mermin
#EPS=$(shell ls *.eps)
TEX=platex
DVIPDF=dvipdfmx

.SUFFIXES: .tex .dvi

all:$(TARGET).dvi

$(TARGET).dvi: $(TARGET).tex $(EPS)

.tex.dvi:
	$(TEX) $<
	$(TEX) $<

tar:
	tar cvzf $(TARGET).tar.gz $(TARGET).* *.eps

pdf: $(TARGET).dvi
	$(DVIPDF) $(TARGET)

clean:
	rm -f $(TARGET).dvi $(TARGET).aux $(TARGET).log 
	rm -f $(TARGET).toc 
	rm -f $(TARGET).pdf $(TARGET).tar.gz 
	rm -f *.pbm *.bmc
