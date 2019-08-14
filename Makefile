run:
	python -m civ6_hooks_matrix mapping.json

init:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

test:
	py.test tests

.PHONY: run init test freeze
