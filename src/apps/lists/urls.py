from django.urls import path
from .views import FavoriteView

urlpatterns = [
    path('favorites/', FavoriteView.as_view()),
]