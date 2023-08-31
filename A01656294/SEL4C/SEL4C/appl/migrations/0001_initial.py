# Generated by Django 4.2.4 on 2023-08-31 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('en_stock', models.BooleanField(default=True)),
            ],
        ),
    ]
