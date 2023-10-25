install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=utils test_*.py

format:
	black . *.py

lint:
	pylint --disable=R,C --extension-pkg-whitelist='pydantic' main.py --ignore-patterns=test_.*?py *.py  utils/*.py

container-lint:
	docker run -rm -i hadolint/hadolint < Dockerfile

refactor:
	format lint

run:
	uvicorn main:app --reload

deploy:
	echo "deploy not implemented"

all: install lint test format deploy
