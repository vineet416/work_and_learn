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
    # If the connection is successful, create a database and collection
    db = client["ticket_management"]
    collection = db["tickets"]