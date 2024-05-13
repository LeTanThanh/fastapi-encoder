from fastapi import FastAPI
from fastapi import Path
from fastapi import Body
from fastapi.encoders import jsonable_encoder

from typing import Annotated


from models.item import Item

app = FastAPI()

items = {}

# Using the jsonable_encoder
@app.put("/items/{id}")
async def update_item(id: Annotated[int, Path()], item: Annotated[Item, Body(embed = True)]):
  dict_item: dict[str, str] = jsonable_encoder(item)
  items[id] = dict_item
  return dict_item
