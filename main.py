import uvicorn
from fastapi import FastAPI
from utils import utils

app = FastAPI()


@app.get("/")
async def root():
    return {"message": utils.hello()}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
