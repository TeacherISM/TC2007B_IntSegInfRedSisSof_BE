# Generated by Django 3.2.12 on 2023-08-28 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20230828_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='edu_lvl',
            field=models.CharField(max_length=100, verbose_name='Máximo nivel educativo'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='gender',
            field=models.CharField(max_length=50, verbose_name='Género'),
        ),
    ]
