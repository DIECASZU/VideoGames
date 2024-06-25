from django.contrib import admin
from .models import Categoria, Juego, Usuario

# Register your models here.


class JuegoAdmin(admin.ModelAdmin):
    list_display = ["codigo", "categoria", "descripcion", "imagen"]
    list_editable = ["imagen"]
    search_fields = ["codigo"]


admin.site.register(Categoria)
admin.site.register(Juego, JuegoAdmin)
admin.site.register(Usuario)
