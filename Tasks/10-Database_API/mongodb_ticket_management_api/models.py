from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class Customer(BaseModel):
    name: str
    email: EmailStr

class Comment(BaseModel):
    text: str

class TicketCreate(BaseModel):
    customer: Customer
    title: str
    description: str
    category: str
    priority: str
    tags: list[str] = []


class TicketUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    priority: Optional[str] = None
    tags: Optional[list[str]] = None

class StatusUpdate(BaseModel):
    status: str