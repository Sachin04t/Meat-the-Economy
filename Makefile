# Variables
ENV_NAME := venv

.DEFAULT_GOAL := help

## Create a virtual environment and install dependencies (cross-platform)
install:
	python -m venv $(ENV_NAME)
	@$(ENV_NAME)/Scripts/python -m pip install -r requirements.txt || \
	$(ENV_NAME)/bin/python -m pip install -r requirements.txt

## Run the analysis (main script)
run: install
	@$(ENV_NAME)/Scripts/python cs506_meattheeconomy.py || \
	$(ENV_NAME)/bin/python cs506_meattheeconomy.py


## Remove the virtual environment (cross-platform)
clean:
	python -c "import shutil; shutil.rmtree('$(ENV_NAME)', ignore_errors=True)"

## Reinstall everything from scratch
reinstall: clean install

## Show help
help:
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}"
