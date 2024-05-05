from sklearn.preprocessing import LabelEncoder
import numpy as np
import faiss
from pymongo import MongoClient
from config import *

class MongoDBToFAISSAdapter:
    def __init__(self, mongodb_uri, mongodb_database):
        self.mongodb_uri = mongodb_uri
        self.mongodb_database = mongodb_database
        self.encoder_dict = {}
        self.index_dict = {}

    def preprocess_data(self, players_data):
        vectors = []
        for player in players_data:
            vector = []
            for attribute, value in player.items():
                if attribute == 'Player':
                    # Guardar el nombre del jugador en el diccionario de codificación
                    if 'Player' not in self.encoder_dict:
                        self.encoder_dict['Player'] = LabelEncoder()
                        # Ajustar el LabelEncoder al nombre del jugador
                        self.encoder_dict['Player'].fit([value])
                    encoded_value = self.encoder_dict['Player'].transform([value])[0]
                    vector.append(encoded_value)
                elif isinstance(value, (int, float)):
                    vector.append(value)
                else:
                    if attribute not in self.encoder_dict:
                        self.encoder_dict[attribute] = LabelEncoder()
                        # Ajustar el LabelEncoder a la característica no numérica
                        self.encoder_dict[attribute].fit([value])
                    encoded_value = self.encoder_dict[attribute].transform([value])[0]
                    vector.append(encoded_value)
            vectors.append(vector)
        return np.array(vectors)

    def build_index(self):
        # Conectar a MongoDB
        client = MongoClient(self.mongodb_uri)
        db = client[self.mongodb_database]
        collections = db.list_collection_names()
        
        for collection_name in collections:
            collection = db[collection_name]

            # Recuperar datos de MongoDB
            players_data = list(collection.find())

            # Preprocesar los datos
            vectors = self.preprocess_data(players_data)

            # Construir índice FAISS
            index = faiss.IndexFlatL2(vectors.shape[1])
            index.add(vectors)

            # Guardar el índice en el diccionario
            self.index_dict[collection_name] = index

    def search_player(self, player_name, collection_name, k=1):
        # Codificar el nombre del jugador
        encoded_player_name = self.encoder_dict['Player'].transform([player_name])[0]

        # Buscar en el índice FAISS correspondiente
        index = self.index_dict[collection_name]
        D, I = index.search(np.array([encoded_player_name]), k)
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
adapter = MongoDBToFAISSAdapter(mongodb_uri, mongodb_database)
adapter.build_index()
player_name = "Lionel Messi"
collection_name = "paris_saint_germain"
distances, indices = adapter.search_player(player_name, collection_name)
print("Distancias:", distances)
print("Índices:", indices)
