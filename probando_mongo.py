from pymongo import MongoClient
from config import username, password
import pandas as pd

uri  = 'mongodb+srv://admin:i9dnviXyDmU14kO8@cluster0.5noc7o6.mongodb.net/'
#.format(username=username, password=password)

# client = MongoClient('localhost', 27017)
client = MongoClient(uri)

db = client['sample_mflix']

print(db.list_collection_names())