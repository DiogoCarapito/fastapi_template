install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#make test with pytest and coverage
	pytest -vv --cov=main --cov=utils test_*.py
	#python -m pytest -vv --cov=main --cov=utils test_*.py

format:
	black . *.py

lint:
	pylint --disable=R,C,W1203 *.py utils/*.py
	# pylint --disable=R,C --extension-pkg-whitelist='pydantic' main.py --ignore-patterns=test_.*?py *.py  utils/*.py

container-lint:
	docker run -rm -i hadolint/hadolint < Dockerfile

refactor:
	format lint

run:
	uvicorn main:app --reload

deploy:
	echo "deploy not implemented"

all: install lint test format deploy
