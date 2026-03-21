from django.db import models
from django.contrib.auth.models import User
from apps.characters.models import Character


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'character')

    def __str__(self):
        return f"{self.user} - {self.character}"


class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ListItem(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('list', 'character')

    def __str__(self):
        return f"{self.list} - {self.character}"