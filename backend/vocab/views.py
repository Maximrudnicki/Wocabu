from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from .models import Word
from .serializers import CreateWordSerializer, WordSerializer


class WordList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        words = Word.objects.filter(user=request.user)
        serializer = WordSerializer(words, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CreateWordSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WordDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        word = get_object_or_404(Word, pk=id, user=request.user)
        serializer = WordSerializer(word)
        return Response(serializer.data)

    def patch(self, request, id):
        word = get_object_or_404(Word, pk=id, user=request.user)
        serializer = WordSerializer(word, data=request.data, partial=True)

        if serializer.is_valid():
            updated_word = serializer.save()

            self.manage_trainings(updated_word)

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        word = Word.objects.get(pk=id, user=request.user)
        word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def manage_trainings(self, word):
        word.is_learned = (
            word.cards
            and word.word_translation
            and word.constructor
            and word.word_audio
        )
        word.save()
