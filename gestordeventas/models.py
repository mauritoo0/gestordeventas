from django.db import models



# Create your models here.

class Vendedores(models.Model):
    nombre = models.CharField(max_length=20)
    correo = models.EmailField(null=True, blank=True)
    

    
    def __str__(self):
        return f'{self.nombre}'
    
class Articulos(models.Model):
    articulo = models.CharField(max_length=20)
    cantidad = models.IntegerField()
    precio_s_iva = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    precio_c_iva = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    
   
    def __str__(self):
        return f'{self.articulo}'
    
class Clientes(models.Model):
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    poblacion = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(null=True, blank=True)
    vendedor = models.ForeignKey(Vendedores, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.nombre}'
    
class Ventas(models.Model):
    vendedor = models.ForeignKey(Vendedores, on_delete=models.SET_NULL, null=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.SET_NULL, null=True)
    articulo = models.ForeignKey(Articulos, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()
    total_venta_s_iva = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    total_venta_c_iva = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    fecha = models.DateField()
    
    def __str__(self):
        fecha_ok = self.fecha.strftime('%d/%m/%Y')
        return f'{fecha_ok} | Vendedor: {self.vendedor}  | Cliente: {self.cliente} || Articulo(s): {self.articulo} | Unidades: {self.cantidad} | '
