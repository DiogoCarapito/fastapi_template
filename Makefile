install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=app --cov=utils tests/*.py

format:
	black . *.py

lint:
	pylint --disable=R,C *.py utils/*.py

container-lint:
	docker run -rm -i hadolint/hadolint < Dockerfile

refactor:
	format lint

deploy:
#echo "deploy not implemented"

all: install lint test format deploy
