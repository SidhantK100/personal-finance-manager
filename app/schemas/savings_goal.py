# schemas/savings_goal.py
from pydantic import BaseModel
from typing import Optional
from datetime import date

class SavingsGoalCreate(BaseModel):
    target_amount: float
    target_date: date

class SavingsGoalResponse(BaseModel):
    id: str
    user_id: str
    target_amount: float
    target_date: date

    class Config:
        orm_mode = True
