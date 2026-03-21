from django.urls import path
from .views import CharacterDetailView

urlpatterns = [
    path('<int:api_id>/', CharacterDetailView.as_view()),
]