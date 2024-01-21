from typing import Annotated
from pydantic import BaseModel

from .ingredient import Ingredient

class Recipe(BaseModel):
    name: str
    ingredients: list[Ingredient]
    steps: list[str]

    def __str__(self):
     return ''