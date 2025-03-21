from pydantic import BaseModel

# Serialization : Model(Complex Obj) -> Python Objs (Dict) -> Json 

class User(BaseModel):
    name: str
    age: int

# Complex obj(Model)
user = User(name="Alice", age=25)

# Convert to dictionary
print(user.model_dump())  
# {'name': 'Alice', 'age': 25}

# Convert to JSON string
print(user.model_dump_json())  
# '{"name": "Alice", "age": 25}'


# Deserialization : Json -> Complex obj

json_data = '{"name": "Bob", "age": 30}'

user = User.model_validate_json(json_data)
print(user)  
# name='Bob' age=30

print(user.name)  # Bob
print(user.age)   # 30
