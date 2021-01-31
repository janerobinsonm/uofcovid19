from flask import Flask
from flask_pymongo import pymongo
from app import app

CONNECTION_STRING = "mongodb+srv://Clariza_Mayo:Foreve6434!@cluster0.y9k04.mongodb.net/<dbname>?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('flask_mongodb_atlas')
user_collection = pymongo.collection.Collection(db, 'user_collection')


# CONNECTION_STRING = "mongodb+srv://Judi_Desire:Foreve6434!@uofcc.g7ndo.mongodb.net/<dbname>?retryWrites=true&w=majority"
# client = pymongo.MongoClient(CONNECTION_STRING)
# db = client.get_database('flask_mongodb_atlas')
# user_collection = pymongo.collection.Collection(db, 'user_collection')

