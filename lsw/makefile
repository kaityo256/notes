TARGET=lswnote
EPS=$(shell ls *.eps)
TEX=platex
DVIPDF=dvipdfmx
DATE=$(shell date +%y%d%m)

.SUFFIXES: .tex .dvi .pdf

all:$(TARGET).pdf
	open $<

$(TARGET).dvi: $(TARGET).tex $(EPS)

.tex.dvi:
	$(TEX) $<
	$(TEX) $<

.dvi.pdf:
	$(DVIPDF) $<

tar:
	tar cvzf $(TARGET).tar.gz $(TARGET).* $(EPS)
	cp $(TARGET).tar.gz $(DATE)$(TARGET).tar.gz

clean:
	rm -f $(TARGET).dvi $(TARGET).aux $(TARGET).log 
	rm -f $(TARGET).pdf $(TARGET).tar.gz 
	rm -f *.pbm *.bmc
