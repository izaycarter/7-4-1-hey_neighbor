from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Tool(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_available = models.BooleanField(default="True")
