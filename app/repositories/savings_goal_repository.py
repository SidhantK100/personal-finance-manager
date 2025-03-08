# repositories/savings_goal_repository.py
from app.utils.database import db
from app.models.savings_goal import SavingsGoal

class SavingsGoalRepository:
    async def create_savings_goal(self, savings_goal: SavingsGoal):
        result = await db['savings_goals'].insert_one(savings_goal.dict())
        return SavingsGoal(**await db['savings_goals'].find_one({'_id': result.inserted_id}))

    async def get_savings_goals(self, user_id: str):
        return await db['savings_goals'].find({'user_id': user_id})

    async def get_savings_goal(self, savings_goal_id: str):
        return await db['savings_goals'].find_one({'_id': savings_goal_id})

    async def update_savings_goal(self, savings_goal_id: str, savings_goal: SavingsGoal):
        await db['savings_goals'].update_one({'_id': savings_goal_id}, {'$set': savings_goal.dict()})
        return await self.get_savings_goal(savings_goal_id)

    async def delete_savings_goal(self, savings_goal_id: str):
        await db['savings_goals'].delete_one({'_id': savings_goal_id})
