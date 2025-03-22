from fastapi import FastAPI

app = FastAPI()

@app.get('/items/{item_id}')
async def root(item_id):
    return {"item_id":item_id}


# define path parameters with types
# cant pass foo as item_id in request "http://127.0.0.1:8000/items/foo" - thorw error
# this type of data validtion is performed by Pydantic under the hood

@app.get('/items/type/{item_id}')
async def path_with_type(item_id : int):
    return {"item_id":item_id}


# predefined path parameters - with Enums
from enum import Enum

class ModelName(str, Enum):
    openai = "openai"
    deepseek = "deepseek"
    llama = "llama"


@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name is ModelName.openai: 
        return {"model_name": model_name, "message": "OpenAi"}

    if model_name.value == "deepseek":  # get value using {model_name.value}
        return {"model_name": model_name, "message": "DeepSeek model"}

    return {"model_name": model_name, "message": "This is Llama"}
