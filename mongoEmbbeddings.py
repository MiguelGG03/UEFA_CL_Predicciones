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
db = client.get_database("champions")
collections = db.list_collection_names()

encoder_dict = {}
attribute_keys = set()

# Initialize and fit encoders for all string attributes
for collection in collections:
    coll = db[collection]
    players_data = list(coll.find({}, {'_id': 0}))
    for player in players_data:
        for key, value in player.items():
            if isinstance(value, str):  # Initialize encoder for string fields
                if key not in encoder_dict:
                    encoder_dict[key] = ExtendedLabelEncoder()
                    all_values = [p[key] for p in players_data if key in p]
                    encoder_dict[key].fit(all_values + ['<unknown>'])  # Add a placeholder for unknown items

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
                vector.append(value)  # If no encoder, append the value directly (possibly replace with handling code)
        vectors.append(vector)

vectors_np = np.array(vectors)
print(vectors_np)
