from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .repositories import WordSetRepository
from .serializers import CreateSetSerializer, SetSerializer


class SetList(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self):
        self.repository = WordSetRepository()

    def get(self, request):
        word_sets = self.repository.get_word_sets_by_user(request.user.id)
        serializer = SetSerializer(word_sets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CreateSetSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            word_set = self.repository.create_word_set(
                name=serializer.validated_data["name"], user_id=request.user.id
            )
            return Response(
                SetSerializer(word_set).data, status=status.HTTP_201_CREATED
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SetDetails(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self):
        self.repository = WordSetRepository()

    def get(self, request, id):
        word_set = self.repository.get_word_set_by_id(id)
        if word_set:
            serializer = SetSerializer(word_set)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        word_set = self.repository.get_word_set_by_id(id)
        if not word_set:
            return Response(
                {"detail": "Set not found."}, status=status.HTTP_404_NOT_FOUND
            )

        update_data = request.data.copy()

        if "user_id" in update_data:
            update_data.pop("user_id")

        updated = self.repository.update_word_set(id, update_data)

        if updated:
            return Response(
                {"detail": "Set updated successfully."}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"detail": "Failed to update set."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def delete(self, request, id):
        word_set = self.repository.get_word_set_by_id(id)
        if word_set:
            deleted = self.repository.delete_word_set(id)
            if deleted:
                return Response(
                    {"detail": "Set deleted successfully."},
                    status=status.HTTP_204_NO_CONTENT,
                )
            else:
                return Response(
                    {"detail": "Failed to delete set."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        else:
            return Response(
                {"detail": "Set not found."}, status=status.HTTP_404_NOT_FOUND
            )


class SetWords(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self):
        self.repository = WordSetRepository()

    def post(self, request, id):
        word_set = self.repository.get_word_set_by_id(id)
        if not word_set:
            return Response({"detail": "Set not found."}, status=status.HTTP_404_NOT_FOUND)

        word_id = request.data.get("word_id")
        if not word_id:
            return Response({"detail": "word_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        if word_id in word_set.words:
            return Response({"detail": "Word is already in the set."}, status=status.HTTP_400_BAD_REQUEST)

        added = self.repository.add_word_to_set(id, word_id)
        if added:
            return Response({"detail": "Word added successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Failed to add word."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def delete(self, request, id):
        word_set = self.repository.get_word_set_by_id(id)
        if not word_set:
            return Response({"detail": "Set not found."}, status=status.HTTP_404_NOT_FOUND)

        word_id = request.data.get("word_id")
        if not word_id:
            return Response({"detail": "word_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        if word_id not in word_set.words:
            return Response({"detail": "Word is missing from the set."}, status=status.HTTP_400_BAD_REQUEST)

        removed = self.repository.remove_word_from_set(id, word_id)
        if removed:
            return Response({"detail": "Word removed successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Failed to remove word."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
