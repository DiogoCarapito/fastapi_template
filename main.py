from fastapi import FastAPI

# from pydantic import BaseModel
import uvicorn

from utils import utils

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": utils.hello()}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
