from django.db import models


class Position(models.Model):
    tittle = models.CharField(max_length=50)

    def __str__(self):
        return self.tittle


class Employee(models.Model):
    nome_completo = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    telefone = models.CharField(max_length=15)
    posição = models.ForeignKey(Position, on_delete=models.CASCADE)
