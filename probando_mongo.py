from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)

db = client['test-database']

collection = db['test-collection']


post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
}

posts = collection
post_id = posts.insert_one(post).inserted_id
post_id