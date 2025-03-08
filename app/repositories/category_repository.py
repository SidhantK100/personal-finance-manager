# repositories/category_repository.py
from app.utils.database import db
from app.models.category import Category

class CategoryRepository:
    async def create_category(self, category: Category):
        result = await db['categories'].insert_one(category.dict())
        return Category(**await db['categories'].find_one({'_id': result.inserted_id}))

    async def get_categories(self):
        return await db['categories'].find()

    async def get_category(self, category_id: str):
        return await db['categories'].find_one({'_id': category_id})

    async def update_category(self, category_id: str, category: Category):
        await db['categories'].update_one({'_id': category_id}, {'$set': category.dict()})
        return await self.get_category(category_id)

    async def delete_category(self, category_id: str):
        await db['categories'].delete_one({'_id': category_id})
