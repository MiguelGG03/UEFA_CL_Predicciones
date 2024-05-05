import faiss
import numpy as np
from pymongo import MongoClient
from config import *

# Connect to MongoDB
uri = "mongodb+srv://{username}:{password}@cluster0.5noc7o6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0".format(username=username, password=password)

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    

db = client.get_database("champions")

all_collections = db.list_collection_names()



# Inicializar un conjunto para almacenar los nombres de los atributos
attributes = set()

for collection in all_collections:
    # Recorrer todos los documentos en la colección
    collection = db[collection]
    for document in collection.find():
        # Agregar los nombres de los atributos del documento al conjunto
        for key in document:
            attributes.add(key)

# Imprimir la lista de atributos
print("Atributos encontrados en los documentos:")
for attribute in attributes:
    print(attribute)