install:
	# install requirements
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		AutoROM -y	

lint:
	# pylint check
	pylint --disable=R,C *.py

format:
	# reformat py codes
	black *.py

test:
	# test if env can be set up successfully
	python -m pytest -vv --cov=setup_env test_setup_env.py

all: install format lint test