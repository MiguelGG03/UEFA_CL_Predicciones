from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np
import faiss
import pymongo
from pymongo import MongoClient
from config import *

class MongoDBToFAISSAdapter:
    def __init__(self, mongodb_uri, mongodb_database, mongodb_collection):
        self.mongodb_uri = mongodb_uri
        self.mongodb_database = mongodb_database
        self.mongodb_collection = mongodb_collection
        self.encoder_dict = {}

    def preprocess_data(self, players_data):
        vectors = []
        for player in players_data:
            vector = []
            for attribute, value in player.items():
                if attribute == 'Player':
                    # Guardar el nombre del jugador en el diccionario de codificación
                    self.encoder_dict['Player'] = LabelEncoder()
                    encoded_value = self.encoder_dict['Player'].fit_transform([value])[0]
                    vector.append(encoded_value)
                elif isinstance(value, (int, float)):
                    vector.append(value)
                else:
                    if attribute not in self.encoder_dict:
                        self.encoder_dict[attribute] = OneHotEncoder(sparse=False, handle_unknown='ignore')
                        encoded_value = self.encoder_dict[attribute].fit_transform([[value]])[0]
                    else:
                        encoded_value = self.encoder_dict[attribute].transform([[value]])[0]
                    vector.extend(encoded_value)
            vectors.append(vector)
        return np.array(vectors)

    def build_index(self):
        # Conectar a MongoDB
        client = pymongo.MongoClient(self.mongodb_uri)
        db = client[self.mongodb_database]
        collection = db[self.mongodb_collection]

        # Recuperar datos de MongoDB
        players_data = list(collection.find())

        # Preprocesar los datos
        vectors = self.preprocess_data(players_data)

        # Construir índice FAISS
        index = faiss.IndexFlatL2(vectors.shape[1])
        index.add(vectors)
        return index

    def search_player(self, player_name, k=1):
        # Codificar el nombre del jugador
        encoded_player_name = self.encoder_dict['Player'].transform([player_name])[0]

        # Buscar en el índice FAISS
        D, I = self.index.search(np.array([encoded_player_name]), k)
        return D, I

# Uso del adaptador
uri = "mongodb+srv://{username}:{password}@cluster0.5noc7o6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0".format(username=username, password=password)

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.get_database("champions")
mongodb_uri = uri
mongodb_database = "champions"
all_collections = db.list_collection_names()
for collection in all_collections:
    adapter = MongoDBToFAISSAdapter(mongodb_uri, mongodb_database, collection)
    index = adapter.build_index()

# Buscar un jugador por nombre
player_name = "Lionel Messi"
distances, indices = adapter.search_player(player_name)
print("Distancias:", distances)
print("Índices:", indices)
