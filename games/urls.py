from django.urls import path, include
from .views import juegos, registro, inicio_sesion, adventure, fighting, moba, rpg, shooter, survival, JuegoViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('juego', JuegoViewset)

urlpatterns = [
    path('', juegos, name="juegos"),
    path('juegos/registro', registro, name="registro"),
    path('inicio_sesion/', inicio_sesion, name="inicio_sesion"),
    path('juegos/adventure', adventure, name="adventure"),
    path('juegos/fighting', fighting, name="fighting"),
    path('juegos/moba', moba, name="moba"),
    path('juegos/rpg', rpg, name="rpg"),
    path('juegos/shooter', shooter, name="shooter"),
    path('juegos/survival', survival, name="survival"),
    path('api/', include(router.urls)),
]
