# repositories/transaction_repository.py
from app.utils.database import db
from app.models.transaction import Transaction

class TransactionRepository:
    async def create_transaction(self, transaction: Transaction):
        result = await db['transactions'].insert_one(transaction.dict())
        return Transaction(**await db['transactions'].find_one({'_id': result.inserted_id}))

    async def get_transactions(self, user_id: str):
        return await db['transactions'].find({'user_id': user_id})

    async def get_transaction(self, transaction_id: str):
        return await db['transactions'].find_one({'_id': transaction_id})

    async def update_transaction(self, transaction_id: str, transaction: Transaction):
        await db['transactions'].update_one({'_id': transaction_id}, {'$set': transaction.dict()})
        return await self.get_transaction(transaction_id)

    async def delete_transaction(self, transaction_id: str):
        await db['transactions'].delete_one({'_id': transaction_id})
