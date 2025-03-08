# services/category_service.py
from app.models.category import Category
from app.repositories.category_repository import CategoryRepository

class CategoryService:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    async def create_category(self, category_data: dict):
        category = Category(**category_data)
        return await self.category_repository.create_category(category)

    async def get_categories(self):
        return await self.category_repository.get_categories()

    async def update_category(self, category_id: str, category_data: dict):
        category = await self.category_repository.get_category(category_id)
        if category:
            updated_category = Category(**category.dict())
            updated_category.name = category_data.get('name', updated_category.name)
            updated_category.description = category_data.get('description', updated_category.description)
            return await self.category_repository.update_category(category_id, updated_category)
        else:
            return None

    async def delete_category(self, category_id: str):
        return await self.category_repository.delete_category(category_id)
