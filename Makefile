.PHONY: help docs
.DEFAULT_GOAL := help


define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
    match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
    if match:
        target, help = match.groups()
        print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:  ## Show this help message
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

docs:  ## generate Sphinx HTML documentation, including API docs
	rm -f docs/fusepystarter*.rst
	sphinx-apidoc -o docs/ fusepystarter/
	rm -f docs/fusepystarter.decorators.rst
	rm -f docs/fusepystarter.cookiecutter.rst
	rm -f docs/fusepystarter.rst
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html
