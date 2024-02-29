install:
	@echo "Installing..."
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	@echo "Installed"

format:
	@echo "Formatting..."
	black *.py */*.py
	@echo "Formatted"

lint:
	@echo "Linting..."
	pylint --disable=R,C *.py */*.py
	@echo "Linted"

test:
	@echo "Testing..."
	pytest -v tests/*.py
	@echo "Tested"

all: install format lint test