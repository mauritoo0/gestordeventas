from django.shortcuts import get_object_or_404, render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Vendedores, Articulos, Ventas, Clientes
from .forms import NuevoVendedor, NuevoArticulo, NuevaVenta, EliminarVenta, EliminarVendedor, EliminarArticulo, NuevoCliente, EliminarCliente, FormularioPersonalizado, LoginPersonalizado, EditarPerfil, EditarVenta, EditarVendedor, EditarCliente, EditarArticulo, BuscarVendedor, BuscarArticulo, BuscarVenta, BuscarCliente
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from decimal import Decimal
from django.db.models import Q



# Create your views here.

def index(request):
    title = "Bienvenido al gestor de ventas"
    return render(request, 'index.html', {
        'title': title
    })


def principal(request):
    title = "Bienvenido"
    vendedores = Vendedores.objects.all()
    ventas = Ventas.objects.all()
    
    return render(request, 'principal.html', {
        'title': title,
        'vendedores': vendedores,
        'ventas': ventas,
        
    })


@login_required 
def vendedores(request):
    title = "Listado de vendedores"
    form = BuscarVendedor(request.GET or None)
    vendedor = Vendedores.objects.all().order_by('-id')
    
    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')
        if nombre:
            vendedor = vendedor.filter(nombre__icontains=nombre)
    
    return render(request, 'vendedores/vendedores.html', {
        'vendedores': vendedor,
        'form': form,
        'title': title
    })


@login_required 
def articulos(request):
    title = "Listado de artículos"
    form = BuscarArticulo(request.GET or None)
    articulos = Articulos.objects.all().order_by('-id')
    
    if form.is_valid():
        articulo_nombre = form.cleaned_data.get('nombre_articulo')
        if articulo_nombre:
            articulos = articulos.filter(articulo__icontains=articulo_nombre)
            
    
    return render(request, 'articulos/articulos.html', {
        'articulos': articulos,
        'form': form,
        'title': title
    })

   
@login_required       
def ventas(request):
    title = "Listado de ventas"
    form = BuscarVenta(request.GET or None)
    venta = Ventas.objects.all().order_by('-id')
    if form.is_valid():
        venta_filtrada = form.cleaned_data.get('b_venta')
        if venta_filtrada:
            venta = venta.filter(
                Q(vendedor__nombre__icontains=venta_filtrada) |
                Q(cliente__nombre__icontains=venta_filtrada)  |
                Q(articulo__articulo__icontains=venta_filtrada) 
                )
    return render(request, 'ventas/ventas.html', {
        'ventas': venta,
        'form': form,
        'title': title
    })
    
    
@login_required 
def clientes(request):
    title = "Listado de clientes"
    form = BuscarCliente(request.GET or None)
    cliente = Clientes.objects.all().order_by('-id')
    if form.is_valid():
        cliente_filtrado = form.cleaned_data.get('cliente')
        if cliente_filtrado:
            cliente = cliente.filter(
                Q(nombre__icontains=cliente_filtrado) |
                Q(apellidos__icontains=cliente_filtrado) |
                Q(direccion__icontains=cliente_filtrado) |
                Q(poblacion__icontains=cliente_filtrado) |
                Q(telefono__icontains=cliente_filtrado) |
                Q(correo__icontains=cliente_filtrado) |
                Q(vendedor__nombre__icontains=cliente_filtrado) 
                )
    
    return render(request, 'clientes/clientes.html', {
        'clientes': cliente,
        'form': form,
        'title': title
    })


@login_required
def nuevo_vendedor(request):
    title = "Nuevo vendedor"
    if request.method =='GET':
        return render(request, 'vendedores/nuevo_vendedor.html', {
            'form': NuevoVendedor(),
            'title': title
    })    
    else:
        Vendedores.objects.create(nombre=request.POST['nombre'], correo=request.POST['correo'])    
        return redirect('vendedores')
        

@login_required
def eliminar_vendedor(request, vendedor_id):
    vendedor = get_object_or_404(Vendedores, id=vendedor_id)
    
    if request.method == "POST":
        
        form = EliminarVendedor(request.POST)
        if form.is_valid() and 'eliminar' in request.POST:
            vendedor.delete()
            return redirect('vendedores')  
    else:
        form = EliminarVendedor()

    return render(request, 'vendedores.html', {'form': form, 'vendedor': vendedor})       
        
        
@login_required
def editar_vendedor(request, vendedor_id):
    title = "Editar vendedor"
    vendedor = get_object_or_404(Vendedores, id=vendedor_id)
    
    if request.method == 'POST':
        form = EditarVendedor(request.POST, instance=vendedor)
        if form.is_valid():
            vendedor.nombre = form.cleaned_data['nombre']
            vendedor.correo = form.cleaned_data['correo']
            vendedor.save()
            
            return redirect ('vendedores')
    else:
        form = EditarVendedor(instance=vendedor)  

    
    return render(request, 'vendedores/editar_vendedor.html', 
                  {'form': form, 'title': title})
   

@login_required
def nuevo_articulo(request):
    title = "Nuevo artículo"
    if request.method == 'POST':
        form = NuevoArticulo(request.POST)
        if form.is_valid():
            articulo = form.cleaned_data['articulo']
            cantidad = form.cleaned_data['cantidad']
            precio_s_iva = form.cleaned_data['precio_s_iva']
            precio_c_iva = precio_s_iva * 1.21  

            
            Articulos.objects.create(
                articulo=articulo,
                cantidad=cantidad,
                precio_s_iva=precio_s_iva,
                precio_c_iva=precio_c_iva
            )

            return redirect('articulos')
    else:
        form = NuevoArticulo()

    return render(request, 'articulos/nuevo_articulo.html', 
                {'form': form,
                 'title': title,
                })
    
  
@login_required  
def eliminar_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulos, id=articulo_id)
    
    if request.method == "POST":
        
        form = EliminarArticulo(request.POST)
        if form.is_valid() and 'eliminar' in request.POST:
            articulo.delete()
            return redirect('articulos')  
    else:
        form = EliminarArticulo()

    return render(request, 'articulos.html', {'form': form, 'articulo': articulo})   


@login_required
def editar_articulo(request, articulo_id):
    title = "Editar artículo"
    artic = get_object_or_404(Articulos, id=articulo_id)
    
        
    if request.method == 'POST':
        form = EditarArticulo(request.POST, instance=artic)
        if form.is_valid():
            articulo = form.cleaned_data['articulo']
            cantidad = form.cleaned_data['cantidad']
            precio_s_iva = form.cleaned_data['precio_s_iva']
            
            
            artic.articulo = articulo
            artic.cantidad = cantidad
            artic.precio_s_iva = Decimal(precio_s_iva)
            artic.precio_c_iva = precio_s_iva * Decimal('1.21')
            artic.save()
            
            return redirect ('articulos')
    else:
        form = EditarArticulo(instance=artic)
        
    return render(request, 'articulos/editar_articulo.html', 
                  {'form': form,
                   'title': title
                   })
         
         
@login_required
def nuevo_cliente(request):
    title = "Nuevo cliente"
    if request.method =='GET':
        return render(request, 'clientes/nuevo_cliente.html', {
            'form': NuevoCliente(),
            'title': title
    })    
    else:
        form = NuevoCliente(request.POST)  
        if form.is_valid():  
            nombre = form.cleaned_data['nombre']
            apellidos = form.cleaned_data['apellidos']
            direccion = form.cleaned_data['direccion']
            poblacion = form.cleaned_data['poblacion']
            telefono = form.cleaned_data['telefono']
            correo = form.cleaned_data['correo']
            vendedor = form.cleaned_data['vendedor']  
            

                        
            Clientes.objects.create(
                nombre=nombre,
                apellidos=apellidos,
                direccion=direccion,
                poblacion=poblacion,
                telefono=telefono,
                correo=correo,
                vendedor=vendedor,  
                
            )

            return redirect('clientes')    
    
        return render(request, 'clientes/nuevo_cliente.html', 
                      {'form': form,
                       'title': title
                       })

     
@login_required
def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Clientes, id=cliente_id)

    if request.method == "POST":
        
        form = EliminarCliente(request.POST)
        if form.is_valid() and 'eliminar' in request.POST:
            cliente.delete()  
            return redirect('clientes')  
    else:
        form=EliminarCliente()

    return render(request, 'clientes.html', {'cliente': cliente})


@login_required
def editar_cliente(request, cliente_id):
    title = "Editar cliente"
    cliente = get_object_or_404(Clientes, id=cliente_id)
    
    if request.method == 'POST':
        form = EditarCliente(request.POST, instance=cliente)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellidos = form.cleaned_data['apellidos']
            direccion = form.cleaned_data['direccion']
            poblacion = form.cleaned_data['poblacion']
            telefono = form.cleaned_data['telefono']
            correo = form.cleaned_data['correo']
            vendedor = form.cleaned_data['vendedor']
            
            cliente.nombre = nombre
            cliente.apellidos = apellidos
            cliente.direccion = direccion
            cliente.poblacion = poblacion
            cliente.telefono = telefono
            cliente.correo = correo
            cliente.vendedor = vendedor
            cliente.save()
            
            return redirect('clientes')

    else:
        form = EditarCliente(instance=cliente)
    
    return render(request, 'clientes/editar_cliente.html', 
                  {'form': form,
                   'title': title
                   })
         
         
@login_required
def nueva_venta(request):
    title = "Nueva venta"
    if request.method =='GET':
        return render(request, 'ventas/nueva_venta.html', {
            'form': NuevaVenta(),
            'title': title
    })    
    else:
        form = NuevaVenta(request.POST)  
        if form.is_valid():  
            vendedor = form.cleaned_data['vendedor']
            cliente = form.cleaned_data['cliente']  
            articulo = form.cleaned_data['articulo']  
            cantidad = form.cleaned_data['cantidad']
            fecha = form.cleaned_data['fecha']
            
            
            total_venta_s_iva = float(articulo.precio_s_iva) * cantidad
            total_venta_c_iva = float(articulo.precio_c_iva) * cantidad
            
            
            articulo.cantidad -= cantidad
            articulo.save()
            
            Ventas.objects.create(
                vendedor=vendedor,
                cliente=cliente,  
                articulo=articulo,  
                cantidad=cantidad,
                total_venta_c_iva=total_venta_c_iva,
                total_venta_s_iva=total_venta_s_iva,
                fecha=fecha
            )

            return redirect('ventas')    
    
        return render(request, 'ventas/nueva_venta.html', 
                      {'form': form,
                       'title': title
                       })


@login_required
def eliminar_venta(request, venta_id):
    venta = get_object_or_404(Ventas, id=venta_id)
    
    if request.method == "POST":
        
        form = EliminarVenta(request.POST)
        if form.is_valid() and 'eliminar' in request.POST:
            venta.delete()
            return redirect('ventas')  
    else:
        form = EliminarVenta()

    return render(request, 'ventas.html', {'form': form, 'venta': venta})

 
@login_required
def editar_venta(request, venta_id):
    title = "Editar venta"
    venta = get_object_or_404(Ventas, id=venta_id)
    
    if request.method == 'POST':
        form = EditarVenta(request.POST, instance=venta)
        if form.is_valid():
            articulo = form.cleaned_data['articulo']
            cantidad = form.cleaned_data['cantidad']
            
            total_venta_s_iva = float(articulo.precio_s_iva) * cantidad
            total_venta_c_iva = float(articulo.precio_c_iva) * cantidad
            
            venta.articulo = articulo
            venta.cantidad = cantidad
            venta.total_venta_s_iva = total_venta_s_iva
            venta.total_venta_c_iva = total_venta_c_iva
            
            venta.save()
            
            return redirect('ventas')
    else:
        form = EditarVenta(instance=venta)
    
    return render(request, 'ventas/editar_venta.html', 
                  {'form': form,
                   'title': title
                   })

  

def register(request):
    title = "Regístrate"
    if request.method == 'POST':
        form = FormularioPersonalizado(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    else:
        form = FormularioPersonalizado()
    return render(request, 'registration/register.html', 
                {'mostrar_navbar':False, 
                'form': form,
                'title': title,
                })


def login_personalizado(request):
    title = 'Ingresa'
    if request.method == 'POST':
        form = LoginPersonalizado(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('principal')
        
    else:
        form = LoginPersonalizado()

    return render(request, 'registration/login.html', 
                  {'mostrar_navbar':False, 
                   'form': form,
                   'title': title
                   })


def logout_view(request):
    logout(request)
    return redirect('index')


@login_required
def editar_perfil(request):
    title = "Editar perfil"
    if request.method == 'POST':
        form = EditarPerfil(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = EditarPerfil(instance=request.user)
        
    return render(request, 'editar_perfil.html', 
                  {'form': form,
                   'title': title
                   })


@login_required
def perfil(request):
    user = request.user
    title = f'Perfil de {user.username}'
    return render(request, 'perfil.html', 
                  {'user': request.user,
                   'title': title
                   })

            
        