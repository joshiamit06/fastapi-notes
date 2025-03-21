# 3. Custom Validators

from pydantic import BaseModel, validator

class User(BaseModel):
    name: str
    age: int

    @validator("age")
    def age_check(cls, value):
        if value < 18:
            raise ValueError("Age must be at least 18")
        return value
    
user = User(name="Bob",age=17)
print(user) # raises error "Age must be at least 18"