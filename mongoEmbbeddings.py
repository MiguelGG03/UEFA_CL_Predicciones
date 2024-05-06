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

    # Initialize and fit encoders for all attributes based on the first document to generalize for all string attributes
    if players_data:
        for key in players_data[0]:
            if isinstance(players_data[0][key], str):  # Check if the attribute is a string
                encoder_dict[key] = LabelEncoder()
                all_values = [player[key] for player in players_data if key in player]
                encoder_dict[key].fit(all_values)

    # Process each player's data
    for player in players_data:
        vector = []
        for attribute, value in player.items():
            if isinstance(value, str):
                # Transform the string value using the pre-fitted LabelEncoder
                if attribute in encoder_dict:  # Ensure the encoder was created for this attribute
                    encoded_value = encoder_dict[attribute].transform([value])[0]
                    vector.append(encoded_value)
                else:
                    # If somehow the attribute was missed in the encoder setup, print a warning
                    print(f"Warning: No encoder found for {attribute}. Skipping this attribute.")
            elif isinstance(value, (int, float)):  # Directly append numerical attributes
                vector.append(value)
            else:
                # If the value is neither string nor numeric (unlikely in this context), you can decide to skip or handle it separately
                print(f"Unhandled data type for attribute {attribute}: {type(value)}. Skipping.")
        vectors.append(vector)

    # Convert the list of lists into a NumPy array
    vectors_np = np.array(vectors)
    print(vectors_np)
