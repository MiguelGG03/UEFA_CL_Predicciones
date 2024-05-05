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

all_data = []

# Recuperar datos de MongoDB
collections = db.list_collection_names()

for collection in collections:
    collection = db[collection]
    data = list(collection.find({}, {"_id": 0}))
    all_data.extend(data)



# Preprocesamiento de datos y construcción de vectores
vectors = faiss.preprocess_data(all_data)

# Construir índice FAISS
index = faiss.IndexFlatL2(vectors.shape[1])
index.add(vectors)

# Guardar el índice FAISS
faiss.write_index(index, "football_players_index.index")

