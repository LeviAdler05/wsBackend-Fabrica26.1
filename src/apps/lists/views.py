from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


from .models import Favorite
from .serializers import FavoriteSerializer
from apps.characters.services import get_or_create_character


class FavoriteView(APIView):

    def get(self, request):
        favorites = Favorite.objects.filter(user=request.user)
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data)

    def post(self, request):
        api_id = request.data.get("api_id")

        if not api_id:
            return Response({"error": "api_id é obrigatório"}, status=400)

        character = get_or_create_character(api_id)

        user = User.objects.first()

        favorite, created = Favorite.objects.get_or_create(
            user=user,
            character=character
)

        if not created:
            return Response({"message": "Já favoritado"})

        serializer = FavoriteSerializer(favorite)
        return Response(serializer.data, status=201)

    def delete(self, request):
        api_id = request.data.get("api_id")

        try:
            favorite = Favorite.objects.get(
                user=request.user,
                character__api_id=api_id
            )
            favorite.delete()
            return Response({"message": "Removido"})
        except Favorite.DoesNotExist:
            return Response({"error": "Não encontrado"}, status=404)