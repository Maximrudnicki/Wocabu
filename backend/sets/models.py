from datetime import datetime


class WordSet:
    def __init__(self, name, user_id, _id=None, words=None):
        self._id = _id
        self.name = name
        self.user_id = user_id
        self.created_at = datetime.now()
        self.words = words if words is not None else []

    def to_dict(self):
        return {
            "id": str(self._id),
            "name": self.name,
            "user_id": self.user_id,
            "created_at": self.created_at.isoformat(),
            "words": self.words,
        }
    
    @classmethod
    def from_dict(cls, word_set_data):
        word_set = cls(
            name=word_set_data["name"],
            user_id=word_set_data["user_id"],
            words=word_set_data.get("words", [])
        )
        word_set._id = word_set_data["_id"]
        word_set.created_at = word_set_data["created_at"]
        return word_set
