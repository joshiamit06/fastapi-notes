'''
Dependencies : Allows to reuse logic such as authentication, db connection, validation
across multiple routes.

1. Ways to inject dependencies:
    1. Depends() - Traditional method
    2. Annotated[] - Newer, preferred method
'''

# Using Depends

from fastapi import FastAPI, Depends, Header, APIRouter, Request
from fastapi.responses import JSONResponse
from typing import Annotated
from fastapi.exceptions import HTTPException
from contextlib import asynccontextmanager
from sqlalchemy.orm import Session
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

def get_username():
    return "JohnDoe" # this return value is injected as username in read_user function

@app.get("/user/")
def read_user(username: str = Depends(get_username)):
    return {"username": username}


# Using Annotated
# Using annotated is more readable and preferrable as it ensures proper type hints.
def get_annotated_username() -> str:
    return "JohnDoe"

UsernameDep = Annotated[str, Depends(get_annotated_username)]

@app.get("/annotated/user/")
def read_annotated_user(username: UsernameDep):
    return {"username": username}


'''
Types of Dependencies : 
A. Function Dependencies - Most common way to reuse logic.
B. Class-Based Dependencies - Useful for stateful data like database sessions. 
                              Managing database connections, config settings, cache.
C. Dependencies with Parameters - Reuse query parameters across multiple endpoints.
D. Sub-Dependencies (Dependency Injection) - Authentication chaining.
E. Yield-Based Dependencies (For Cleanup) - Useful for database connections, file handling, API calls.
                                            Automatic resource cleanup.
                                            
'''

# Function Dependencies
def get_api_key(api_key: str = Header(...)):
    if api_key != "my-secret-key":
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key

@app.get("/secure/")
def read_secure_data(api_key: str = Depends(get_api_key)):
    return {"message": "Authorized"}


# Class based dependencies
class Database:
    def __init__(self):
        self.connection = "Connected to DB"

    def __call__(self):
        return self.connection

db_dependency = Database()

@app.get("/db/")
def get_db(db: str = Depends(db_dependency)):
    return {"db_status": db}


# Dependencies with parameters
def pagination(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

PaginationDep = Annotated[dict, Depends(pagination)]

@app.get("/items/")
def read_items_pagination(pagination: PaginationDep):
    return {"message": "Paginated Items", "params": pagination}



# Sub-Dependencies

def get_api_key(api_key: str = Header(...)):
    return api_key

def get_user(api_key: str = Depends(get_api_key)):
    return {"user": "admin", "api_key": api_key}

@app.get("/profile/")
def read_profile(user: dict = Depends(get_user)):
    return user


# Yield-Based Dependencies
def get_db_yield():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@app.get("/db_users/")
def read_users_w_db_session(db: Session = Depends(get_db_yield)):
    return {"db_status": "Session active"}


# Global dependencies

router = APIRouter(dependencies=[Depends(get_api_key)])

@router.get("/data/")
def read_data():
    return {"message": "Authorized"}


# Middleware with dependencies 
class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        token = request.headers.get("Authorization")
        if token != "Bearer secret-token":
            return JSONResponse(status_code=403, content={"detail": "Forbidden"})
        response = await call_next(request)
        return response

app.add_middleware(AuthMiddleware)
