from django.db import models
from uuid import uuid4


class Cliente(models.Model):
    objects = None
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=60, null=True)
    email = models.CharField(max_length=50, null=True)
    cpf = models.CharField(max_length=14, null=True)

    def __str__(self) -> str:
        return self.nome


class Produtos(models.Model):
    objects = None
    codigo = models.CharField(max_length=20, null=False)
    descricao = models.CharField(max_length=60, null=False)

    def __str__(self) -> str:
        return self.codigo

