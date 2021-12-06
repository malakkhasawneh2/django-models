from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import CharField
# Create your models here.

class Snack(models.Model):
    name=models.CharField(max_length=255)
    purchaser=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description=models.CharField(max_length=255)

    def __str__(self):
        return self.name

