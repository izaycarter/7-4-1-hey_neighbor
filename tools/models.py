from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Tool(models.Model):
    HAND_TOOL = "HAND TOOL"
    GARDEN_TOOL = "GARDEN TOOL"
    POWER_TOOL = "POWER TOOL"


    Type_Choices = [
        (HAND_TOOL,"Hand Tool"),
        (GARDEN_TOOL, "Garden Tool"),
        (POWER_TOOL, "Power Tool"),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=Type_Choices, default=HAND_TOOL)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_available = models.BooleanField(default="False")
