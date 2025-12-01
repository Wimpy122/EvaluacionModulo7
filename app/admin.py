from django.contrib import admin
from .models import Producto, Categoria, Etiqueta, DetalleProducto
# Register your models here.

class DetalleProductoInline(admin.StackedInline):
    model = DetalleProducto
    can_delete = False
    verbose_name_plural = 'Detalles Técnicos'


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'created_at') 
    list_filter = ('categoria', 'created_at') 
    search_fields = ('nombre', 'descripcion') 
    inlines = [DetalleProductoInline]
    filter_horizontal = ('etiquetas',) 

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)
admin.site.register(Etiqueta)