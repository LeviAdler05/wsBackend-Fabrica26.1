from django.urls import path
from .views import CharacterDetailView, CharacterListView

urlpatterns = [
    path('', CharacterListView.as_view()),
    path('<int:api_id>/', CharacterDetailView.as_view()),
]