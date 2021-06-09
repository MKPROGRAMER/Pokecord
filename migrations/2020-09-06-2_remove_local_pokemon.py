"""
This is a one-shot script used to migrate all Pokémon from array fields to a global collection.
6 September 2020
"""

import config
from pymongo import MongoClient

client = MongoClient(config.DATABASE_URI)
db = client[config.DATABASE_NAME]

result = db["member"].update_many({}, {"$unset": {"pokemon": 1}})
