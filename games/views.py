from django.shortcuts import render
from .models import Juego
from .forms import UsuarioForm
from rest_framework import viewsets
from .serializers import JuegoSerializer

# Create your views here.


class JuegoViewset(viewsets.ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer


def juegos(request):
    return render(request, 'games/index.html')


def inicio_sesion(request):
    return render(request, 'games/inicio_sesion.html')


def registro(request):
    data = {
        'form': UsuarioForm()
    }

    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Registro Guardado con Exito"
        else:
            data["form"] = formulario

    return render(request, 'games/registro.html', data)


def adventure(request):
    return render(request, 'games/adventure.html')


def fighting(request):
    return render(request, 'games/fighting.html')


def moba(request):
    return render(request, 'games/moba.html')


def rpg(request):
    return render(request, 'games/rpg.html')


def shooter(request):
    return render(request, 'games/shooter.html')


def survival(request):
    return render(request, 'games/survival.html')
