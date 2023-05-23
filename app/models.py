from django.db import models

class UserModel(models.Model):
    nome = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)

class CarroModel(models.Model):
    nome = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    modelo = models.CharField(max_length=254)
    cor = models.CharField(max_length=254)


class GaragemModel(models.Model):
    numero = models.PositiveIntegerField()