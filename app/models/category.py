# models/category.py
from pydantic import BaseModel
from typing import Optional

class Category(BaseModel):
    id: Optional[str]
    name: str
    description: str

class CategoryInDB(Category):
    class Config:
        orm_mode = True
