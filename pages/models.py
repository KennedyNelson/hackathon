from django.conf import settings
from django.db import models


class Farmer(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    item = models.CharField(max_length=255)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.name
# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title