# Generated by Django 4.2.4 on 2023-08-25 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PCMaster",
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
                ("procesador", models.CharField(max_length=50)),
                ("tarjetaGrafica", models.CharField(max_length=50)),
                ("NumVentiladores", models.IntegerField()),
                ("FuentePoder", models.CharField(max_length=50)),
                ("FechaConsulta", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
