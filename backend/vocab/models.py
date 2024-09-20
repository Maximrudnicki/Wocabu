from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Word(models.Model):
    word = models.CharField(max_length=255, unique=True, db_index=True)
    definition = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    is_learned = models.BooleanField(default=False)
    cards = models.BooleanField(default=False)
    word_translation = models.BooleanField(default=False)
    constructor = models.BooleanField(default=False)
    word_audio = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"<Word(id={self.id}, word={self.word}, definition={self.definition}, user_id={self.user.id}>"
