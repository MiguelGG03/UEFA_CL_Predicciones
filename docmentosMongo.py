from pymongo.mongo_client import MongoClient
from config import *
import json
import os

uri = "mongodb+srv://{username}:{password}@cluster0.5noc7o6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0".format(username=username, password=password)

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    

db = client.get_database("champions")


documents = list(db['real_madrid'].find({}, {"_id": 0}))

print(json.dumps(documents, indent=4, sort_keys=True, default=str))
