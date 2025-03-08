# services/transaction_service.py
from app.models.transaction import Transaction
from app.repositories.transaction_repository import TransactionRepository

class TransactionService:
    def __init__(self, transaction_repository: TransactionRepository):
        self.transaction_repository = transaction_repository

    async def create_transaction(self, transaction_data: dict):
        transaction = Transaction(**transaction_data)
        return await self.transaction_repository.create_transaction(transaction)

    async def get_transactions(self, user_id: str):
        return await self.transaction_repository.get_transactions(user_id)

    async def update_transaction(self, transaction_id: str, transaction_data: dict):
        transaction = await self.transaction_repository.get_transaction(transaction_id)
        if transaction:
            updated_transaction = Transaction(**transaction.dict())
            updated_transaction.amount = transaction_data.get('amount', updated_transaction.amount)
            updated_transaction.transaction_date = transaction_data.get('transaction_date', updated_transaction.transaction_date)
            updated_transaction.category = transaction_data.get('category', updated_transaction.category)
            updated_transaction.description = transaction_data.get('description', updated_transaction.description)
            return await self.transaction_repository.update_transaction(transaction_id, updated_transaction)
        else:
            return None

    async def delete_transaction(self, transaction_id: str):
        return await self.transaction_repository.delete_transaction(transaction_id)
