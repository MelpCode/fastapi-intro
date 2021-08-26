from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost/'

client = MongoClient(MONGO_URI)

#Create the database
dbc = client["fastapi-contacts"]

