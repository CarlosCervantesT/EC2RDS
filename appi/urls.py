from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.home, name='home'),

    # CRUD Clientes
    path('registrar_cliente/', views.registrarCliente, name='registrar_cliente'),
    path('editar_cliente/', views.editar_cliente, name='editar_cliente'),
    path('eliminar_cliente/', views.eliminar_cliente, name='eliminar_cliente'),
    path('listar_clientes/', views.listar_clientes, name='listar_clientes'),

    # CRUD Productos
    path('registrar_producto/', views.registrar_producto, name='registrar_producto'),
    path('editar_producto/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/', views.eliminar_producto, name='eliminar_producto'),
    path('listar_productos/', views.listar_productos, name='listar_productos'),

    # CRUD Facturas
    path('registrar_factura/', views.registrar_factura, name='registrar_factura'),
    path('editar_factura/', views.editar_factura, name='editar_factura'),
    path('eliminar_factura/', views.eliminar_factura, name='eliminar_factura'),
    path('listar_facturas/', views.listar_facturas, name='listar_facturas'),

    # Reportes
    path('productos_mas_vendidos/', views.mas_vendidos, name='productos_mas_vendidos'),
    path('top_clientes/', views.listar_topClientes, name='top_clientes'),
]
