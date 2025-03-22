from fastapi import FastAPI

app = FastAPI()

# query params : http://127.0.0.1:8000/items/?skip=0&limit=10 
# naturally string but they are converted to that type and validated against it.
# they are not a fixed part of a path, they can be optional and can have default values.
# below ex. they have default values of skip=0 and limit=10.
# http://127.0.0.1:8000/items/ is same as http://127.0.0.1:8000/items/?skip=0&limit=10
# http://127.0.0.1:8000/items/?skip=20 -> param value in function is skip=20 and limit=10


@app.get('/items')
async def read_items(skip: int = 0, limit: int = 10):
    return {"skip":skip,"limit":limit}



# Optional query params by setting default to None
@app.get("/items/{item_id}")
async def read_items_optional(item_id: str, q: str | None = None):
    if q:
        return {"item_id":{item_id}, "q":q}
    return {"item_id":item_id}



# required query params
# If you don't want to add a specific value but just make it optional, set the default as None.
# when you want to make a query parameter required, you can just not declare any default value.
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item