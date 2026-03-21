from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CharacterSerializer
from .services import get_or_create_character


class CharacterDetailView(APIView):
    def get(self, request, api_id):
        try:
            character = get_or_create_character(api_id)
            serializer = CharacterSerializer(character)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )