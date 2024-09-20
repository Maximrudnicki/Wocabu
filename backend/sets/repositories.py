from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

from .models import WordSet

client = MongoClient("mongodb://localhost:27017/")
db = client['pardodb']
word_sets_collection = db['word_sets']


class WordSetRepository:
    def __init__(self, collection=word_sets_collection):
        self.collection = collection

    def create_word_set(self, name, user_id, words=None):
        # word_set = {
        #     "name": name,
        #     "user_id": user_id,
        #     "words": words if words else [],
        #     "created_at": datetime.now(),
        # }
        word_set = WordSet(name=name, user_id=user_id, words=words) 
        result = self.collection.insert_one(word_set)
        word_set["_id"] = str(result.inserted_id)
        return word_set

    def get_word_sets_by_user(self, user_id):
        word_sets = self.collection.find({"user_id": user_id})
        return [self._convert_id(word_set) for word_set in word_sets]

    def get_word_set_by_id(self, word_set_id):
        word_set = self.collection.find_one({"_id": ObjectId(word_set_id)})
        if word_set:
            return self._convert_id(word_set)
        return None

    def delete_word_set(self, word_set_id):
        result = self.collection.delete_one({"_id": ObjectId(word_set_id)})
        return result.deleted_count > 0

    def update_word_set(self, word_set_id, update_data):
        result = self.collection.update_one(
            {"_id": ObjectId(word_set_id)},
            {"$set": update_data}
        )
        return result.modified_count > 0

    def add_word_to_set(self, word_set_id, word_id):
        result = self.collection.update_one(
            {"_id": ObjectId(word_set_id)},
            {"$addToSet": {"words": word_id}}
        )
        return result.modified_count > 0

    def remove_word_from_set(self, word_set_id, word_id):
        result = self.collection.update_one(
            {"_id": ObjectId(word_set_id)},
            {"$pull": {"words": word_id}}
        )
        return result.modified_count > 0

    def _convert_id(self, word_set):
        word_set["id"] = str(word_set["_id"])
        del word_set["_id"]
        return word_set