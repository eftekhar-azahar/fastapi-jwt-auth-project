from product.models import Product
from pydantic import BaseModel
from typing import Optional

class Display_seller(BaseModel):
    username:str
    email:str

    class Config:
        orm_mode = True

class Product(BaseModel):
    name: str
    description: str
    price: int
    

    class Config:
        from_attributes = True

class DisplayProduct(BaseModel):
    name: str
    description: str
    price: int

    class Config:
        from_attributes = True


class Seller(BaseModel):
    username:str
    email:str
    password:str

    class Config:
        orm_mode = True

class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    username:Optional[str]=None