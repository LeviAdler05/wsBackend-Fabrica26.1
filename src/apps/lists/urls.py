from django.urls import path
from .views import FavoriteView, ListView, ListItemView

urlpatterns = [
    path('favorites/', FavoriteView.as_view()),
    path('', ListView.as_view()),
    path('<int:list_id>/items/', ListItemView.as_view()),
]