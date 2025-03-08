# schemas/transaction.py
from pydantic import BaseModel
from typing import Optional
from datetime import date

class TransactionCreate(BaseModel):
    amount: float
    transaction_date: date
    category: str
    description: str

class TransactionResponse(BaseModel):
    id: str
    user_id: str
    amount: float
    transaction_date: date
    category: str
    description: str

    class Config:
        orm_mode = True
