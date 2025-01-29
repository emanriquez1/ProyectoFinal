from django.contrib import admin

# Register your models here.
from .models import Medida

@admin.register(Medida)
class MedidaAdmin(admin.ModelAdmin):
    list_display = ('id_medida', 'tipo', 'nombre', 'indicador', 'formula', 'frecuencia', 'verificacion')