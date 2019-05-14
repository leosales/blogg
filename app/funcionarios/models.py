from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Funcionario(models.Model):
    matricula = models.DecimalField(max_digits=6, decimal_places=0)
    nome = models.CharField(max_length=30)
    cpf = models.DecimalField(max_digits=11, decimal_places=0)
    rg = models.DecimalField(max_digits=11, decimal_places=0)
    carga_horaria = models.IntegerField()
    salario = models.DecimalField(max_digits=20, decimal_places=0)
    cargo = models.ForeignKey('Cargo', verbose_name='Cargo', on_delete=CASCADE)


    def __str__(self):
        return self.nome


class Cargo(models.Model):
    codigo = models.CharField(max_length=20)
    bio = models.TextField()


class ContraCheque(models.Model):
    # salario = models.ForeignKey('Funcionario', verbose_name='salario', on_delete=CASCADE)

    def contribuicao(self, salario):
        SalarioLiquido = salario - 79.20
