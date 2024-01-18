from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/steps/{step_id}")
def read_step(step_id: int, q: Union[str, None] = None):
    return {"step_id": step_id, "q": q}


@app.get("/ingredients/{ingredient_id}")
def read_ingredient(ingredient_id: int, q: Union[str, None] = None):
    return {"ingredient_id": ingredient_id, "q": q}
