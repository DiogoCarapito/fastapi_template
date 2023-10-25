[![Github Actions Workflow](https://github.com/DiogoCarapito/fastapi_template/actions/workflows/main.yaml/badge.svg)](https://github.com/DiogoCarapito/fastapi_template/actions/workflows/main.yaml)

# FastAPI template

Template of a FastAPI Python Microservice ready to deploy using Docker

From Coursera's **MLOps | Machine Learning Operations** by Duke University

# Cheat sheet

### virtual environement

```bash
virtualenv ~/.venv
source ~/.venv/bin/activate
nano ~/.bashrc
```

add to the bottom

```text
# Source VirtualENV
source ~/.venv/bin/activate
```

### docker
```bash
docker build .
docker image ls
# Copy IMAGE ID
docker run -p 127.0.0.1:8080:8080  <IMAGE ID>
```
