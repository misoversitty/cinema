.PHONY = all build virtualenv run debug


build: virtualenv
	. .venv/bin/activate
	pip install poetry
	poetry update
	echo 'Done installing dependencies'

virtualenv:
	python3 -m venv .venv

clean:
	rm -rf .venv
