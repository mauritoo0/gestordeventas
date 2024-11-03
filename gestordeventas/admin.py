from django.contrib import admin
from .models import *

# Register your models here.


class VendedoresAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo')
    search_fields = ('nombre', 'correo')  

admin.site.register(Vendedores, VendedoresAdmin)


class ArticulosAdmin(admin.ModelAdmin):
    list_display = ('articulo', 'cantidad', 'precio_s_iva', 'precio_c_iva')
    search_fields = ('articulo',)  # Permite buscar por el campo 'articulo'

admin.site.register(Articulos, ArticulosAdmin)


class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'direccion', 'poblacion', 'telefono', 'correo', 'vendedor')
    search_fields = ('nombre', 'apellidos', 'correo', 'poblacion')  

admin.site.register(Clientes, ClientesAdmin)


class VentasAdmin(admin.ModelAdmin):
    
    def fecha_ok(self, obj):
        return obj.fecha.strftime('%d/%m/%Y')
    
    fecha_ok.short_description = 'Fecha'
    
    list_display = ('id','fecha_ok', 'cliente', 'articulo', 'cantidad', 'total_venta_s_iva', 'total_venta_c_iva', 'vendedor')
    
    search_fields = ('id','fecha', 'cliente', 'articulo', 'vendedor')  

admin.site.register(Ventas, VentasAdmin)