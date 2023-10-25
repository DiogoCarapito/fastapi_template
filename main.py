from fastapi import FastAPI
from utils import utils

app = FastAPI()


@app.get("/")
async def root():
    return {"message": utils.hello()}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
