SHELL = /bin/bash
PYTHON := python3
PIP := pip3
FILES_PATH := backend/app
TESTS_PATH := backend/tests

.PHONY: help lint test setup clean
.ONESHELL: setup clean

help:
	@echo "~~~~~~~~~~~~~~~~~~~~~~~HELP~~~~~~~~~~~~~~~~~~~~~~~~"
	@echo "lint : run code linters and formatters."
	@echo "test : run tests."
	@echo "setup : prepares the enviornment to load the project."
	@echo "clean : cleans the environment."
	@echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

lint:
	${PYTHON} -m autoflake ${FILES_PATH}
	${PYTHON} -m isort ${FILES_PATH}
	${PYTHON} -m black ${FILES_PATH}
	${PYTHON} -m mypy ${FILES_PATH}
	${PYTHON} -m pylint ${FILES_PATH}
	${PYTHON} -m flake8 ${FILES_PATH}

test:
	${PYTHON} -m pytest ${TESTS_PATH}

setup:
	echo "placeholder"

clean: setup
	echo "placeholder"