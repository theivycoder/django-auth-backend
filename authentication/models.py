from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_TYPE = [
        ('DM', 'Dungeon Master'),
        ('PC', 'Player Character'),
    ]
    user_type = models.CharField(
        max_length=2,
        choices=USER_TYPE,
        default='DM',
    )
