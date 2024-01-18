from typing import Union

from fastapi import FastAPI
from db.db import get_database
from bson.objectid import ObjectId

app = FastAPI()
db = get_database()

@app.get("/")
def read_root():
    return {"Hello": "World", "hey": "hey hey"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/steps/{step_id}")
def read_step(step_id: int, q: Union[str, None] = None):
    return {"step_id": step_id, "q": q}


@app.get("/dev_add/") # Don't use GET for inserting
def add_recipe(q: Union[str, None] = None):
    if not q:
        ## Uncomment to add a recipe for testing
        # recipe = {
        #     "title": "Peanut Butter and Jelly Sandwich",
        #     "ingredients": [
        #         "bread", "peanut butter", "jelly"
        #     ],
        #     "steps": [
        #         "Spread peanut butter on one piece of bread",
        #         "Spread jelly on the other piece of bread",
        #         "Put the two pieces of bread together",
        #     ],
        # }

        # recipe_id = db['collection'].insert_one(recipe).inserted_id

        return {"recipe_id": "probably use id: '65a98d81599dbd86154b1b97'"}

    else:
        recipe = db['collection'].find_one({"_id": ObjectId(q)})

        return { "recipe": {
            **recipe,
            "_id": f"{recipe['_id']}"
        } }