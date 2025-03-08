# repositories/user_repository.py
from app.utils.database import db
from app.models.user import User

class UserRepository:
    async def create_user(self, user: User):
        result = await db['users'].insert_one(user.dict())
        return User(**await db['users'].find_one({'_id': result.inserted_id}))

    async def get_user(self, user_id: str):
        return await db['users'].find_one({'_id': user_id})

    async def update_user(self, user_id: str, user: User):
        await db['users'].update_one({'_id': user_id}, {'$set': user.dict()})
        return await self.get_user(user_id)

    async def delete_user(self, user_id: str):
        await db['users'].delete_one({'_id': user_id})
