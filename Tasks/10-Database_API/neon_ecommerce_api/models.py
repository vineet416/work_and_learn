from pydantic import BaseModel, Field, EmailStr
from typing import List


# User Models
class UserCreate(BaseModel):
    name: str
    email: EmailStr


# Product Models
class InventoryUpdate(BaseModel):
    inventory: int = Field(ge=0)


# Order Models
class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)


class OrderCreate(BaseModel):
    user_id: int
    items: List[OrderItemCreate]