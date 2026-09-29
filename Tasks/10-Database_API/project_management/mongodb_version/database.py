from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()
# Get the MongoDB connection URI from environment variables
uri = os.getenv("MONGO_DB_URL")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Test the connection
try:
    client.admin.command('ping')
except Exception as e:
    raise Exception(f"Error connecting to MongoDB: {e}")
else:
    # Select database
    database = client["task_management"]
    # Collections
    projects_collection = database["projects"]
    tasks_collection = database["tasks"]