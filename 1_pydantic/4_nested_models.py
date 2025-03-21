from pydantic import BaseModel

class Address(BaseModel):
    city: str
    zipcode: int

class User(BaseModel):
    name: str
    address: Address

user = User(name="Amit", address={"city":"Pune", "zipcode":"411001"})

print(user) # name='Amit' address=Address(city='Pune', zipcode=411001)