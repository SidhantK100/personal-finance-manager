# services/savings_goal_service.py
from app.models.savings_goal import SavingsGoal
from app.repositories.savings_goal_repository import SavingsGoalRepository

class SavingsGoalService:
    def __init__(self, savings_goal_repository: SavingsGoalRepository):
        self.savings_goal_repository = savings_goal_repository

    async def create_savings_goal(self, savings_goal_data: dict):
        savings_goal = SavingsGoal(**savings_goal_data)
        return await self.savings_goal_repository.create_savings_goal(savings_goal)

    async def get_savings_goals(self, user_id: str):
        return await self.savings_goal_repository.get_savings_goals(user_id)

    async def update_savings_goal(self, savings_goal_id: str, savings_goal_data: dict):
        savings_goal = await self.savings_goal_repository.get_savings_goal(savings_goal_id)
        if savings_goal:
            updated_savings_goal = SavingsGoal(**savings_goal.dict())
            updated_savings_goal.target_amount = savings_goal_data.get('target_amount', updated_savings_goal.target_amount)
            updated_savings_goal.target_date = savings_goal_data.get('target_date', updated_savings_goal.target_date)
            return await self.savings_goal_repository.update_savings_goal(savings_goal_id, updated_savings_goal)
        else:
            return None

    async def delete_savings_goal(self, savings_goal_id: str):
        return await self.savings_goal_repository.delete_savings_goal(savings_goal_id)
