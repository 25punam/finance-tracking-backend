from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = (
        ("viewer", "Viewer"),
        ("analyst", "Analyst"),
        ("admin", "Admin"),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="viewer"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username