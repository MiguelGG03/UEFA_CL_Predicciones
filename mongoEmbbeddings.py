from sklearn.preprocessing import LabelEncoder
import numpy as np
from pymongo.mongo_client import MongoClient
from config import *

class ExtendedLabelEncoder(LabelEncoder):
    def __init__(self, *args, **kwargs):
        super(ExtendedLabelEncoder, self).__init__(*args, **kwargs)
        self.classes_ = None

    def fit(self, y):
        super().fit(y)
        self.classes_ = np.append(self.classes_, '<unknown>')

    def transform(self, y):
        new_y = np.array([item if item in self.classes_ else '<unknown>' for item in y])
        return super().transform(new_y)

uri = "mongodb+srv://{username}:{password}@cluster0.5noc7o6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0".format(username=username, password=password)
client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Error conectando a MongoDB:", e)
    
db = client.get_database("champions")
collections = db.list_collection_names()
print("Colecciones disponibles:", collections)

encoder_dict = {}
attribute_keys = set()

for collection in collections:
    coll = db[collection]
    players_data = list(coll.find({}, {'_id': 0}))
    print(f"Datos en {collection}:", players_data)
    if not players_data:
        continue  # Si no hay datos, pasa a la siguiente colección
    for player in players_data:
        for key, value in player.items():
            if isinstance(value, str):  # Initialize encoder for string fields
                if key not in encoder_dict:
                    all_values = [p[key] for p in players_data if key in p]
                    encoder_dict[key] = ExtendedLabelEncoder()
                    encoder_dict[key].fit(all_values + ['<unknown>'])
                    print(f"Encoder para {key} entrenado con valores: {encoder_dict[key].classes_}")

# Second pass: Encode data
vectors = []
for collection in collections:
    coll = db[collection]
    players_data = list(coll.find({}, {'_id': 0}))
    for player in players_data:
        vector = []
        for key in attribute_keys:
            value = player.get(key, '<unknown>')  # Use '<unknown>' as a default for missing values
            if key in encoder_dict:
                encoded_value = encoder_dict[key].transform([value])[0]
                vector.append(encoded_value)
            else:
                vector.append(value)  # If no encoder, append the value directly
        vectors.append(vector)
        print(f"Vector for player {player.get('name', 'Unknown')}: {vector}")

vectors_np = np.array(vectors)
print("Array final:", vectors_np)
