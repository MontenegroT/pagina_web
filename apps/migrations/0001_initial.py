# Generated by Django 4.1.5 on 2023-03-10 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='libros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('autor', models.CharField(max_length=30)),
                ('genero', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('usename', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('contrasena', models.CharField(max_length=30)),
            ],
        ),
    ]