import numpy as np
from sklearn.preprocessing import LabelEncoder
from pymongo.mongo_client import MongoClient
from config import *

# MongoDB connection string setup
uri = "mongodb+srv://{username}:{password}@cluster0.5noc7o6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0".format(username=username, password=password)
client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Connect to the database and get collection names
db = client.get_database("champions")
collections = db.list_collection_names()

# Dictionary to store LabelEncoders for each attribute
encoder_dict = {}

for collection in collections:
    collection = db[collection]
    # Retrieve data from MongoDB
    players_data = list(collection.find({}, {'_id': 0}))

    # Initialize vectors list to store encoded data
    vectors = []

    # Check if 'Player' encoder has been created and fit it with all player names in the dataset
    if 'Player' not in encoder_dict:
        encoder_dict['Player'] = LabelEncoder()
        all_players = [player['Player'] for player in players_data]  # List all player names
        encoder_dict['Player'].fit(all_players)  # Fit the encoder with all player names

    # Process each player's data
    for player in players_data:
        vector = []
        for attribute, value in player.items():
            if attribute == 'Player':
                # Transform the player's name using the pre-fitted LabelEncoder
                encoded_value = encoder_dict['Player'].transform([value])[0]
                vector.append(encoded_value)
            elif isinstance(value, (int, float)):  # Directly append numerical attributes
                vector.append(value)
            else:
                # Encode other categorical attributes
                if attribute not in encoder_dict:
                    encoder_dict[attribute] = LabelEncoder()
                    # Fit the encoder to the attribute values
                    attr_values = [p[attribute] for p in players_data]
                    encoder_dict[attribute].fit(attr_values)
                encoded_value = encoder_dict[attribute].transform([value])[0]
                vector.append(encoded_value)
        vectors.append(vector)

    # Convert the list of lists into a NumPy array
    vectors_np = np.array(vectors)
    print(vectors_np)
