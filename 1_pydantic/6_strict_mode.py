from pydantic import BaseModel, Field

class User(BaseModel):
    age: int

user = User(age="25")  # Converts "25" to int

class StrictUser(BaseModel):
    age: int = Field(..., strict=True)

StrictUser(age="25")  # Raises error: Input should be a valid integer
