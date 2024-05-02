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

for collection_ in collections:
    # Seleccionar la colección
    collection = db[collection_]

    # Eliminar el campo 'edad' de todos los documentos
    result = collection.update_many({}, {'$unset': {'Unnamed: 0': 1}})

    # Imprimir el número de documentos actualizados
    print('Documentos actualizados:', result.modified_count)
