from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

MONGO_URI = os.getenv('MONGO_URI')

if not MONGO_URI:
    raise ValueError("MONGO_URI is not set in .env file")

client = AsyncIOMotorClient(MONGO_URI)
db = client['personal_finance_manager']
