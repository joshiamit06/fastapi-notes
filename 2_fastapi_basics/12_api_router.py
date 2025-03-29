from fastapi import FastAPI
from routes.users import user_router
from routes.products import product_router

app = FastAPI()

# Include routers
app.include_router(user_router, prefix="/users")
app.include_router(product_router, prefix="/products")

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI"}


'''
To include router in main.py follow below project structure

my_project/
│── main.py
│── routes/
│   ├── users.py
│   ├── products.py


## routes/users.py

from fastapi import APIRouter

user_router = APIRouter()

@user_router.get("/users")
async def get_users():
    return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

    
## routes/products.py

from fastapi import APIRouter

product_router = APIRouter()

@product_router.get("/products")
async def get_products():
    return [{"id": 101, "name": "Laptop"}, {"id": 102, "name": "Phone"}]


'''