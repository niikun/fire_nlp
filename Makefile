install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	python -m textblob.download_corpora

format:
	black *.py
	
lint:
	pylint --disable=R,C *.py
	
test:
	python -m pytest -vv *.py
	
all: install lint test format