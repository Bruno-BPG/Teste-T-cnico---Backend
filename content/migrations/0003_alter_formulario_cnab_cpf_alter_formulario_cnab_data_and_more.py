# Generated by Django 4.1 on 2022-11-25 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0002_alter_formulario_cnab_cartao"),
    ]

    operations = [
        migrations.AlterField(
            model_name="formulario_cnab",
            name="cpf",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="formulario_cnab",
            name="data",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="formulario_cnab",
            name="hora",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="formulario_cnab",
            name="natureza",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="formulario_cnab",
            name="sinal",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="formulario_cnab",
            name="valor",
            field=models.CharField(max_length=50),
        ),
    ]