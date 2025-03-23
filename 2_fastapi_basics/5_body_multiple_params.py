from typing import Annotated

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# mix path, query and body params
@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None, # set body parameters as optional
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results




# can also declare multiple body parameters, e.g. item and user

class NewItem(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None

# Can except json body as per
'''
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
}
'''

@app.put("/items/multi-body/{item_id}")
async def update_item_w_multi_bdoy(item_id: int, item: NewItem, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results



# Singular values in body
# If want to add another key "importance" in the same body with NewItem and User model
# you can instruct FastAPI to treat it as another body key using Body

# it will expect json body as per

'''
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance": 5
}
'''
@app.put("/items/singular/{item_id}")
async def update_item_singular(
    item_id: int,
    item: Item, 
    user: User, 
    importance: Annotated[int, Body()]  #it will treat/expect importance as a body param
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results