from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField()
    self_prove = models.CharField(max_length=50)
    self_prove_answer = models.CharField(max_length=50)

    def __str__(self):
        return self.username

