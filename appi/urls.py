from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.home, name='home'),

    # CRUD Clientes
    path('registrar_cliente/', views.registrarCliente, name='registrar_cliente'),
    path('editar_cliente/', views.editarCliente, name='editar_cliente'),
    path('eliminar_cliente/', views.eliminarCliente, name='eliminar_cliente'),
    path('listar_clientes/', views.listarClientes, name='listar_clientes'),

    # CRUD Productos
    path('registrar_producto/', views.registrarProducto, name='registrar_producto'),
    path('editar_producto/', views.editarProducto, name='editar_producto'),
    path('eliminar_producto/', views.eliminarProducto, name='eliminar_producto'),
    path('listar_productos/', views.listarProductos, name='listar_productos'),

    # CRUD Facturas
    path('registrar_factura/', views.registrarFactura, name='registrar_factura'),
    path('editar_factura/', views.editarFactura, name='editar_factura'),
    path('eliminar_factura/', views.eliminarFactura, name='eliminar_factura'),
    path('listar_facturas/', views.listarFacturas, name='listar_facturas'),

    # Reportes
    path('productos_mas_vendidos/', views.mas_vendidos, name='productos_mas_vendidos'),
    path('top_clientes/', views.listar_topClientes, name='top_clientes'),
]
