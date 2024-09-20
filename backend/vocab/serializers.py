from rest_framework import serializers

from .models import Word


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word

        fields = (
            "id",
            "word",
            "definition",
            "created_at",
            "is_learned",
            "cards",
            "word_translation",
            "constructor",
            "word_audio",
        )

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class CreateWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word

        fields = ("word", "definition")

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
