[![Github Actions Workflow](https://github.com/DiogoCarapito/fastapi_template/actions/workflows/main.yaml/badge.svg)](https://github.com/DiogoCarapito/fastapi_template/actions/workflows/main.yaml)

# FastAPI template

Template of a FastAPI Python Microservice ready to deploy using Docker

From Coursera's **MLOps | Machine Learning Operations** by Duke University

# Cheat sheet

### virtual environement

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
````

```bash
#nano ~/.bashrc
```

add to the bottom
```mk
# Source VirtualENV
#source ~/.venv/bin/activate
```

### docker
```bash
docker build -t main .
docker images
# Copy IMAGE ID
docker run -p 127.0.0.1:8080:8080 <IMAGE ID>
```

api is now available at 
[http://127.0.0.1:8080/](http://127.0.0.1:8080/)

api docs are now available at
[http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs)