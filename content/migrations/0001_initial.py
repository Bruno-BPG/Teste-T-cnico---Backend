# Generated by Django 4.1 on 2022-11-25 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Formulario_CNAB",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tipo", models.CharField(max_length=50)),
                ("data", models.CharField(max_length=15)),
                ("natureza", models.CharField(max_length=10)),
                ("sinal", models.CharField(max_length=2)),
                ("valor", models.IntegerField()),
                ("cpf", models.CharField(max_length=12)),
                ("cartao", models.CharField(max_length=15)),
                ("hora", models.CharField(max_length=10)),
                ("dono_nome", models.CharField(max_length=50)),
                ("nome_loja", models.CharField(max_length=50)),
            ],
        ),
    ]
