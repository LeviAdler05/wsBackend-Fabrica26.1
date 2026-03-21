import requests
from django.conf import settings
from .models import Character

BASE_URL = "https://rickandmortyapi.com/api/character"


def fetch_character_from_api(api_id: int) -> dict:
    url = f"{BASE_URL}/{api_id}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.RequestException:
        raise Exception("Erro ao conectar com API externa")

    return response.json()


def get_or_create_character(api_id: int) -> Character:
    """
    Busca personagem no banco ou cria via API
    """

    # 1. tenta buscar no banco
    try:
        return Character.objects.get(api_id=api_id)
    except Character.DoesNotExist:
        pass

    # 2. se não existir, busca na API
    data = fetch_character_from_api(api_id)

    # 3. salva no banco
    character = Character.objects.create(
        api_id=data["id"],
        name=data["name"],
        status=data["status"],
        species=data["species"],
        gender=data["gender"],
        image=data["image"],
    )

    return character