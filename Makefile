
.PHONY: build upload

build:
	python setup.py sdist bdist_wheel

test:
	python -m unittest discover -s tests

upload:
	twine upload dist/*

