# Makefile

# Sphinx build command
SPHINXBUILD = sphinx-build

# Output directories
HTMLBUILDDIR = _build
#PDFBUILDDIR = pdf

# Default target: build HTML and store
html:
	$(SPHINXBUILD) -M html . $(HTMLBUILDDIR)

# Target to build PDF
pdf:
	$(SPHINXBUILD) -b latex . $(PDFBUILDDIR)
	cd $(PDFBUILDDIR) && make

# Clean up build files
clean:
	rm -rf $(HTMLBUILDDIR)/*
	rm -rf $(PDFBUILDDIR)/*

.PHONY: html pdf clean

#sphinx-build -b latex . pdf
#cd pdf
#make
