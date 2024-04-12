from pymongo import MongoClient
import pandas as pd

client = MongoClient('localhost', 27017)

db = client['uefa-database']

df = pd.read_csv('docs\data\clear\goalkeeper\goalkeeper.csv')

teams = df['Club'].unique().tolist()

teams.append("Arsenal")

for team in teams:
    temp = db["{team}".format(team=team)]
    
madrid = db["Real Madrid"]

madrid.insert_one({})