from typing import Annotated
from pydantic import BaseModel

from .unit import Unit

class Ingredient(BaseModel):
    name: str
    amount: float | int | None
    unit: Unit | None

