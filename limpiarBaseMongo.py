from pymongo.mongo_client import MongoClient
from config import *


uri = "mongodb+srv://{username}:{password}@cluster0.5noc7o6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0".format(username=username, password=password)

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    

db = client.get_database("champions")

collections = ['real_madrid','paris_saint_germain','borussia_dormund','bayern_munich']

def main_1(db, collections):
    for collection_ in collections:
        collection = db[collection_]
        result = collection.update_many({}, {'$unset': {'Unnamed: 0': 1}})
        print('Documentos actualizados:', result.modified_count)

def main_2(db, collections):
    for collection in collections:
        collection = db[collection]
        result = collection.update_many({},{'$unset': {'Pos': ""}})
        print('Documentos actualizados:', result.modified_count)


#main_1(db, collections)
main_2(db, collections)