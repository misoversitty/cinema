VENV_DIR=./.venv


.PHONY = all install virtualenv run debug

all: install

debug: SHELL:=/bin/bash
debug: virtualenv
	source $(VENV_DIR)/bin/activate; \
	python3 src/main.py

install: SHELL:=/bin/bash
install: virtualenv
	source $(VENV_DIR)/bin/activate; \
	pip install poetry; \
	poetry install --no-root

virtualenv:
	test -d $(VENV_DIR) || python3 -m venv $(VENV_DIR)

clean:
	rm -rf $(VENV_DIR)
