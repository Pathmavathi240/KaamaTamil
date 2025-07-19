import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_DB_URI")
mongo_client = pymongo.MongoClient(MONGO_URI)
db = mongo_client["vc_music"]
log_col = db["logs"]

def connect_mongo():
    return db

def log_song(chat_id, user_id, title):
    log_col.insert_one({
        "chat_id": chat_id,
        "user_id": user_id,
        "title": title
    })
