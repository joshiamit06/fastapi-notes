from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    name: str
    age: Optional[int] = 18 # Default age is 18

user = User(name="user")
print(user.age) # 18


# This can be also done with Field class

class FieldUser(BaseModel):
    name: str = Field(..., alias="fullName")  # Required field (...)
    age: int = Field(default=18)  # Optional with default

# This will raise an error because `name` is required
user = User(age=25)  
# ValidationError: name field required

# Correct usage
user = User(name="Alice")
print(user)  # name='Alice' age=18