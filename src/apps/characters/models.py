from django.db import models


class Character(models.Model):
    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    species = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    image = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (API ID: {self.api_id})"