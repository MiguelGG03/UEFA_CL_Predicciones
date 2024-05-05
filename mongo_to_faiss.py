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




def preprocess_data(players_data , atributos = ATRIBITOS_DATABASE):
    """
    Preprocesa los datos de los jugadores, manejando datos numéricos y no numéricos.
    
    Args:
    - players_data: Lista de diccionarios donde cada diccionario representa los datos de un jugador.
    
    Returns:
    - player_vectors: Lista de listas que contiene los vectores de datos de los jugadores.
    """

    player_vectors = []

    for player in players_data:
        vector = []
        for attribute in atributos:
            if attribute in player:
                value = player[attribute]
                # Manejar valores no numéricos convirtiéndolos a valores numéricos si es posible
                if isinstance(value, str) and value.isdigit():
                    value = float(value)
                vector.append(value)
            else:
                # Si el jugador no tiene el atributo, agregar un valor predeterminado (por ejemplo, NaN)
                vector.append(float('nan'))
        player_vectors.append(vector)

    return player_vectors



db = client.get_database("champions")

all_data = []

# Recuperar datos de MongoDB
collections = db.list_collection_names()

for collection in collections:
    collection = db[collection]
    data = list(collection.find({}, {"_id": 0}))
    all_data.extend(data)

# Preprocesamiento de datos y construcción de vectores
vectors = preprocess_data(all_data)
print(vectors)

# Convertir la lista de vectores a un array NumPy
vectors_np = np.array(vectors)

# Construir índice FAISS
index = faiss.IndexFlatL2(vectors_np.shape[1])
index.add(vectors_np)

# Guardar el índice FAISS
faiss.write_index(index, "football_players_index.index")

