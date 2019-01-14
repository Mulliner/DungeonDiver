from pymongo import MongoClient
from pymongo import errors

class DungeonDiverDB:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.dungeondiver
    
    def create_character_collection(self):
        collection = self.db.create_collection('Character')
        return collection

    def get_db(self):
        try:
            self.create_character_collection()
        except errors.CollectionInvalid:
            # Character Collection already Exists
            pass
        return self.db
    
    def character_collection(self):
        collection = self.db.get_collection('Character')
        return collection
    
    def restore_character(self):
        collection = self.db.get_collection('Character')
        characters = list()
        cursor = collection.find({})
        for char in cursor:
            characters.append(char)
        return characters
    
    def update_character(self, mongo_id, character):
        collection = self.db.get_collection('Character')
        update = collection.find_one_and_update({"_id": mongo_id}, {"$set": character})
        return update

