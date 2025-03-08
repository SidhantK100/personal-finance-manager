# models/user.py
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str]
    name: str
    email: str
    password: str

class UserInDB(User):
    class Config:
        orm_mode = True
