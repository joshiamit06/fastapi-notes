from typing import Annotated

from fastapi import FastAPI, Header, Cookie

app = FastAPI()


@app.get("/items/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}

'''
if you send header with request
X-Token: foo
X-Token: bar

The response would be like:
{
    "X-Token values": [
        "bar",
        "foo"
    ]
}
'''


# Cookie

@app.get("/items/cookie/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}