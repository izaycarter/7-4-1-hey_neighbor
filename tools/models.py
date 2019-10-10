from django.db import models


# Create your models here.

class Neighbor(models.Model):
    name = models.CharField(max_length=255)
