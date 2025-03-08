# models/savings_goal.py
from pydantic import BaseModel
from typing import Optional
from datetime import date

class SavingsGoal(BaseModel):
    id: Optional[str]
    user_id: str
    target_amount: float
    target_date: date

class SavingsGoalInDB(SavingsGoal):
    class Config:
        orm_mode = True
