from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('principal/', views.principal, name='principal'),
    path('vendedores/', views.vendedores, name='vendedores'),
    path('articulos/', views.articulos, name='articulos'),
    path('ventas/', views.ventas, name='ventas'),
    path('clientes/', views.clientes, name='clientes'),
    path('nuevo_vendedor/', views.nuevo_vendedor, name='nuevo_vendedor'),
    path('nuevo_articulo/', views.nuevo_articulo, name='nuevo_articulo'),
    path('nueva_venta/', views.nueva_venta, name='nueva_venta'),
    path('nuevo_cliente/', views.nuevo_cliente, name='nuevo_cliente'),
    path('eliminar_venta/<int:venta_id>/', views.eliminar_venta, name='eliminar_venta'),
    path('eliminar_vendedor/<int:vendedor_id>/', views.eliminar_vendedor, name='eliminar_vendedor'),
    path('eliminar_articulo/<int:articulo_id>/', views.eliminar_articulo, name='eliminar_articulo'),
    path('eliminar_cliente/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('editar_venta/<int:venta_id>/', views.editar_venta, name='editar_venta'),
    path('editar_vendedor/<int:vendedor_id>/', views.editar_vendedor, name='editar_vendedor'),
    path('editar_cliente/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('editar_articulo/<int:articulo_id>/', views.editar_articulo, name='editar_articulo'),
    path('register/', views.register, name='register'),
    path('login/', views.login_personalizado, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar', views.editar_perfil, name='editar_perfil'),
    
   
    
]