PROJNAME = main

.PHONY: $(PROJNAME).pdf all clean

all: $(PROJNAME).pdf

$(PROJNAME).pdf: $(PROJNAME).tex
	tectonic -X compile $(PROJNAME).tex 2>&1 || tectonic $(PROJNAME).tex

clean:
	rm -f *.aux *.log *.out *.toc *.synctex.gz *.bbl *.blg *.acn *.ist *.glo *.pdf

