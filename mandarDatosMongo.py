from pymongo.mongo_client import MongoClient
from config import *
import json
import os

uri = "mongodb+srv://{username}:{password}@cluster0.5noc7o6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0".format(username=username, password=password)

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    

db = client.get_database("champions")


def insert_data_to_database(db,equipo):
    directory = r'docs\data\equipos_jugadores\{equipo}'.format(equipo=equipo)

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            print(file_path)
            with open(file_path, 'r') as file:
                data = json.load(file)
                db[equipo].insert_one(data)

insert_data_to_database(db,'real_madrid')
insert_data_to_database(db,'paris_saint_germain')
insert_data_to_database(db,'borussia_dormund')
insert_data_to_database(db,'bayern_munich')
