from django.contrib import admin
from django.urls import path
from appi import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Ruta para la página principal
    path('registrar/', views.registrarCliente, name='registrar_cliente')  # Nombre de la vista corregido
]
