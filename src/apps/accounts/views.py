from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"error": "Usuário inválido"}, status=400)

        if not user.check_password(password):
            return Response({"error": "Senha inválida"}, status=400)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key})