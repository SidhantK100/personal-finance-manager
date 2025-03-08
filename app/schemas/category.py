# schemas/category.py
from pydantic import BaseModel
from typing import Optional

class CategoryCreate(BaseModel):
    name: str
    description: str

class CategoryResponse(BaseModel):
    id: str
    name: str
    description: str

    class Config:
        orm_mode = True
