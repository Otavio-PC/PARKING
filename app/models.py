from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        )
    nome = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)

    class Meta:
        db_table = "user"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class CarroModel(models.Model):
    dono = models.ForeignKey(
        UserModel,
        related_name='colecao',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    garagem = models.ForeignKey(
        'GaragemModel',
        related_name='estacionados',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    placa = models.CharField(max_length=254)
    modelo = models.CharField(max_length=254)
    cor = models.CharField(max_length=254)

    class Meta:
        db_table = "carro"
        ordering = ["placa"]

    def __str__(self):
        return self.placa

class GaragemModel(models.Model):
    numero = models.PositiveIntegerField()

    class Meta:
        ordering = ["numero"]

    def __str__(self):
        return str(self.numero)
