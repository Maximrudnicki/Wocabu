from datetime import datetime


class WordSet:
    def __init__(self, name, user_id, words=None):
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
