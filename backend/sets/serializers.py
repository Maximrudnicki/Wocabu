from rest_framework import serializers

from .models import WordSet


class SetSerializer(serializers.Serializer):
    _id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField(read_only=True)
    words = serializers.ListField(default=list)

    def create(self, validated_data):
        validated_data["user_id"] = self.context["request"].user.id
        word_set = WordSet(**validated_data)

        word_set_repository = self.context["word_set_repository"]
        return word_set_repository.create_word_set(
            word_set.name, word_set.user_id, word_set.words
        )

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.words = validated_data.get("words", instance.words)

        word_set_repository = self.context["word_set_repository"]
        word_set_repository.update_word_set(instance.id, instance.to_dict())
        return instance


class CreateSetSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        validated_data["user_id"] = self.context["request"].user.id
        word_set = WordSet(
            name=validated_data["name"], user_id=validated_data["user_id"]
        )

        word_set_repository = self.context["word_set_repository"]
        return word_set_repository.create_word_set(word_set.name, word_set.user_id)

    class Meta:
        fields = "name"
