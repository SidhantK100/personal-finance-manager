# services/user_service.py
from app.models.user import User
from app.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create_user(self, user_data: dict):
        user = User(**user_data)
        return await self.user_repository.create_user(user)

    async def get_user(self, user_id: str):
        return await self.user_repository.get_user(user_id)

    async def update_user(self, user_id: str, user_data: dict):
        user = await self.get_user(user_id)
        if user:
            updated_user = User(**user.dict())
            updated_user.name = user_data.get('name', updated_user.name)
            updated_user.email = user_data.get('email', updated_user.email)
            return await self.user_repository.update_user(user_id, updated_user)
        else:
            return None

    async def delete_user(self, user_id: str):
        return await self.user_repository.delete_user(user_id)
