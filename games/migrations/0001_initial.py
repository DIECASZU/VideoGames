# Generated by Django 5.0.3 on 2024-04-28 21:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=200, unique=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='juegos/')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='juegos', to='games.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('run', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('fechanacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('direccion', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('clave', models.CharField(max_length=255)),
                ('juego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='juegos', to='games.juego')),
            ],
        ),
    ]
