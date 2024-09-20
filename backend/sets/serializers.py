from rest_framework import serializers

from .models import WordSet


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordSet

        fields = ("id", "name", "created_at", "words")

    def create(self, validated_data):
        validated_data["user_id"] = self.context["request"].user_id
        return super().create(validated_data)


class CreateSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordSet

        fields = ("name")

    def create(self, validated_data):
        validated_data["user_id"] = self.context["request"].user_id
        return super().create(validated_data)
