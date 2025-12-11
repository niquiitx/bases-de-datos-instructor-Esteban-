"""seed_mongo.py
Script to load mongodb_inserts.json into appropriate collections.

Requirements:
pip install pymongo
"""

import json
from pymongo import MongoClient
import os

MONGO_URI = os.getenv('MONGO_URI','mongodb://127.0.0.1:27017')
DB = 'appdb'
client = MongoClient(MONGO_URI)
db = client[DB]

with open('mongodb_inserts.json','r', encoding='utf-8') as f:
    docs = json.load(f)

# heuristic: determine collection by keys
for doc in docs:
    if 'bio' in doc or 'preferences' in doc:
        db.user_profiles.insert_one(doc)
        print('Inserted into user_profiles')
    elif 'events' in doc:
        db.activity_logs.insert_one(doc)
        print('Inserted into activity_logs')
    elif 'type' in doc and 'content' in doc:
        db.documents.insert_one(doc)
        print('Inserted into documents')
    else:
        print('Unknown doc shape, inserting into documents by default')
        db.documents.insert_one(doc)
