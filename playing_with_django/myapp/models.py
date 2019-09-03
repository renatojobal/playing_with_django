from django.db import models
from django.contrib.auth.models import AbstractUser

# Heredando de AbstracUser
class UserChild(AbstractUser):

    # Ver si le puedo agregar nuevos atributos
    birthday = models.DateField(blank=True, null=True)
    genre = models.CharField(max_length=1, default='U', blank=True)
    points = models.IntegerField(blank=True, null=True)
