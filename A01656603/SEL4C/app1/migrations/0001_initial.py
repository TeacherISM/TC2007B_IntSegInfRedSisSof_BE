# Generated by Django 4.2.4 on 2023-08-24 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=100)),
                ('user_fname', models.CharField(max_length=100)),
                ('user_lname', models.CharField(max_length=100)),
                ('user_level', models.CharField(max_length=100)),
                ('user_school', models.CharField(max_length=100)),
                ('user_gender', models.CharField(max_length=100)),
                ('user_age', models.IntegerField()),
                ('user_country', models.CharField(max_length=100)),
                ('user_schooln', models.CharField(max_length=100)),
                ('user_notes', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
