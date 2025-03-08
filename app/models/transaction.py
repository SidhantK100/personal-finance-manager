# models/transaction.py
from pydantic import BaseModel
from typing import Optional
from datetime import date

class Transaction(BaseModel):
    id: Optional[str]
    user_id: str
    amount: float
    transaction_date: date
    category: str
    description: str

class TransactionInDB(Transaction):
    class Config:
        orm_mode = True
