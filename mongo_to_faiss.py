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


"""
atributos_proveidos = [
    'xG+/-90', 'Tackles won', 'Assists', 'SoTA', 'Pos', 'Club', 'Position', 'Goals/shot on target','Progressive carries', 'Fouls Drawn', 'Mn/Sub', 'A-xAG', 'Times tackled during takeon (%)', 'Passes completed (long) %', 'CrdYellow', 'Shots on target %', 'xA', 'Expected goal', 'PrgP', 'penalties comitted', 'Passes completed (short) %', 'Goals/shot', 'AvgLen', 'onGA', 'Expected Assist Goals (xAG)', 'Touches (LiveBall)', 'PKA', 'ball recoveries', 'Total carrying distance', 'Total Passes completion %', 'onG', 'PSxG/SoT', 'PKsv', 'xG+/-', 'PSxG+/-', 'Miscontrols', '#OPA/90', 'Clearances', 'Fouls Comitted', 'Compl', 'Dispossessed', 'G+A', 'Stp%', 'Goals', 'Passes into Final third', 'Progressive passes', 'CS%', 'Crosses into Penalty Area', 'Born', 'npxG', 
    'Touches (Mid 3rd)', 'GA90', 'penalties won', 'Touches (Def Pen)', 'Mn/Start', 'FK', 'Penalty kicks attempted', 'PSxG', 'CrdRed', 'D', 'L', 'unSub', 'Key Passes', 'PK', 'PKm', 'Mn/MP', 'Blocks', 'Passes into Penalty Area', 'CK', 'Player', 'Passes completed (medium) %', 'Progressive carrying distance', 'MP', 'Min', 'No. of dribblers tackled', 'Touches (Att 3rd)', 'Opp', 'Save%', 'xG+xAG', 'GA', 'Age', 'Carries into penalty area', 'Interceptions', 'No. of players tackled', 'xAG', '90s', 'own goals', 'Starts', 'Free kicks', 'npxG+xAG', 'Dribbles challenged (total)', 'Touches (Def 3rd)', 'PPM', 'Shot Total', 'Progressive passing distance', 'Crosses', 'Carries', 'xG', 'Shots blocked', 'G-PK', 'Cmp%', 'Passes received', 'Take-ons attempted', 'AvgLen.1', 'Avg shot distance', 'Penalty kicks', 'Gls', '2nd Yellows', 'OG', 'On-Off', 'Shots on target', 'Red Cards', 'onxGA', 'Goals minus expected goals', 'G+A-PK', 'Shots on target/90', 'Shots Total/90', 'Thr', 'W', 'onxG', 'successful takeon (%)', 'challenges lost', 'AvgDist', 'Passes blocked', 'Yellow Cards', 'Ast', '_id', '/90', 'Errors', 'Touches (Att Pen)', 'Touches', 'PrgR', 'Nationality', 'PrgC', '% of dribblers successfully tackled', 'PKatt', 'Carries into final third'
]
"""

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

