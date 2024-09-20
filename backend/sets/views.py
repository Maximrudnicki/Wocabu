from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class WordList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pass

    def post(self, request):
        pass


class WordDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        pass

    def patch(self, request, id):
        pass

    def delete(self, request, id):
        pass

