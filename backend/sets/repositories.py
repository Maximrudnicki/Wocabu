from pymongo import MongoClient
from bson.objectid import ObjectId

from vocab.models import Word
from .models import WordSet

client = MongoClient("mongodb://localhost:27017/")
db = client['pardodb']
word_sets_collection = db['word_sets']


class WordSetRepository:
    def __init__(self, collection=word_sets_collection):
        self.collection = collection

    def create_word_set(self, name, user_id, words=None):
        word_set = WordSet(name=name, user_id=user_id, words=words) 
        result = self.collection.insert_one(word_set.to_dict())
        word_set._id = result.inserted_id
        return word_set
    
    def get_word_sets_by_user(self, user_id):
        word_sets = list(self.collection.find({"user_id": user_id}))
        for set in word_sets: # we need to replace ids with words
            if set:
                words = []
                for word_id in set['words']:
                    try:
                        word = Word.objects.get(pk=word_id)
                        words.append(word.to_dict())
                    except Word.DoesNotExist:
                        continue
                set['words'] = words
        return [WordSet.from_dict(word_set) for word_set in word_sets]

    def get_word_set_by_id(self, word_set_id):
        word_set_data = self.collection.find_one({"_id": ObjectId(word_set_id)})
        if word_set_data: # we need to replace ids with words
            words = []
            for word_id in word_set_data['words']:
                try:
                    word = Word.objects.get(pk=word_id)
                    words.append(word.to_dict())
                except Word.DoesNotExist:
                    continue
            word_set_data['words'] = words
            return WordSet.from_dict(word_set_data)
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
