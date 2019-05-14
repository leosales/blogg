# Generated by Django 2.1.5 on 2019-05-08 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.DecimalField(decimal_places=0, max_digits=6)),
                ('nome', models.CharField(max_length=30)),
                ('cpf', models.DecimalField(decimal_places=0, max_digits=11)),
                ('rg', models.DecimalField(decimal_places=0, max_digits=11)),
                ('carga_horaria', models.IntegerField()),
            ],
        ),
    ]