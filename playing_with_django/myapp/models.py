
# Django
from django.db import models
from django.contrib.auth.models import User


# Modelo Proxy de usuario
class ProxyUser(User):

    # Ver si le puedo agregar nuevos atributos
    birthday = models.DateField()
    genre = models.CharField(max_length=1, blank=True)
    points = models.IntegerField(blank=True)


    # Indicandole que es un proxy
    class Meta:
        proxy = True

