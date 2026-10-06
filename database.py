import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)

db = client["expense_tracker"]

expenses_collection = db["expenses"]
categories_collection = db["categories"]


def test_connection():
    try:
        client.admin.command("ping")
        print("MongoDB Atlas connection successful!")
        return True

    except Exception as e:
        print("MongoDB connection failed:")
        print(e)
        return False


if __name__ == "__main__":
    test_connection()