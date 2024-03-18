from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Picture(models.Model):
    name = models.TextField()
    description = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='pictures'
    )
