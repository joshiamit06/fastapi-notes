"""
What is Pydantic ?

Pydantic is a data validation and settings management library for Python. 
It provides a way to define and enforce data structures using Python type hints.

Features ->

1. Data Validation and Automatic Type Conversion (Coercion)
2. Custom Validators
3. Default Values and Optional Fields , Aliases for Field Names
4. Parsing Complex Data (Nested Models)
5. Serialization and Deserialization
6. Strict Mode
7. Environment Variable Support (Settings Management)

"""

# -------------------------------------------------

#--- 1. Data Validation 2. Automatic Type Conversion (Coercion)

# Before pydantic (Manual Validation)
class User:
    def __init__(self, name:str,age:int):
        if not isinstance(name,str):
            raise ValueError("Name must be a string")
        if not isinstance(age,int):
            raise ValueError("Age must be an integer")

        self.name = name
        self.age = age

user = User("Amit", "30") # This will raise an error "Age must be an integer"

# With Pydantic
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Amit", age="30") # Automatically converts "25" to an integer
print(user) # name='John' age=25
print(user.age, type(user.age))   # 30 <class 'int'>

