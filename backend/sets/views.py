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
            return Response(SetSerializer(word_set).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SetDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        pass

    def patch(self, request, id):
        pass

    def delete(self, request, id):
        pass
