from django.contrib import admin
from .models import Favorite, List, ListItem

admin.site.register(Favorite)
admin.site.register(List)
admin.site.register(ListItem)