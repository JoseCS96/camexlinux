from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from .models import Producto
from .models import TipoDeCultivo
from .models import Cultivo
from .models import Cliente
from .models import Variedade
from .models import FaseCultivo
from .models import Colaborador
from .models import Cosecha


# Register your models here.
admin.site.register(Producto)
admin.site.register(TipoDeCultivo)
admin.site.register(Cultivo)
admin.site.register(Cliente)
admin.site.register(Variedade)
admin.site.register(FaseCultivo)


@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('dni','nombre', 'apellido', 'direccion')
    #ordering = ('nombre','apellido')
    search_fields = ('nombre','apellido')
    list_editable = ('nombre','apellido')

class CosechaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_hora', 'ubicacion', 'mostrar_persona_ejecuta', 'tipo_cultivo', 'variedad')
    
    def mostrar_persona_ejecuta(self, obj):
        return f"{obj.persona_ejecuta.first_name} {obj.persona_ejecuta.last_name}"
    
    mostrar_persona_ejecuta.short_description = 'Persona que ejecuta'

class CosechaResources(resources.ModelResource):
    fields = (
        'fecha_hora',
        'ubicacion',
        'cantidad_cosechada',
        'equipo_utilizado',
        'calidad_cosechado',
        'observaciones',
        'fase',
        'persona_ejecuta',
        'cultivo',
        'variedad',
    )
    class Meta:
        model = Cosecha


@admin.register(Cosecha)
class CosechaAdmin(ImportExportModelAdmin):
    resource_class = CosechaResources
    list_display = ('fecha_hora','ubicacion','cantidad_cosechada','equipo_utilizado','calidad_cosechado','observaciones','fase','persona_ejecuta','cultivo','variedad')
    #ordering = ('nombre','apellido')
    search_fields = ('fecha_hora','cantidad_cosechada')
    #list_editable = ('nombre','apellido')


    
# class Cosecha(models.Model):
#     fecha_hora = models.DateTimeField()
#     ubicacion = models.CharField(max_length=100)
#     cantidad_cosechada = models.PositiveIntegerField()
#     equipo_utilizado = models.CharField(max_length=100)
#     calidad_cosechado = models.CharField(max_length=20)
#     observaciones = models.TextField()
#     fase = models.ForeignKey('FaseCultivo', on_delete=models.CASCADE)
#     persona_ejecuta = models.ForeignKey(Colaborador, on_delete=models.CASCADE, default=1)
#     cultivo = models.ForeignKey('Cultivo', on_delete=models.CASCADE, default=1)
#     variedad = models.ForeignKey('Variedade', on_delete=models.CASCADE)
    
#     def __str__(self):
#         return f"Cosecha - {self.fecha_hora}"