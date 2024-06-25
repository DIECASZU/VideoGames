from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Juego(models.Model):
    codigo = models.CharField(max_length=200, unique=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='juegos/', null=True, blank=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name='juegos')

    def __str__(self):
        return self.get_code_name()

    def get_code_name(self):
        return f" Codigo: {self.codigo} - {self.nombre}"


class Usuario(models.Model):
    run = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    fechanacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    direccion = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    clave = models.CharField(max_length=255)
    juego = models.ForeignKey(
        Juego, on_delete=models.CASCADE, related_name='juegos')

    def __str__(self):
        return self.nombre
