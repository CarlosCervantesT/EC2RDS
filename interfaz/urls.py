# interfaz/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appi.urls')),  # Importa TODAS las rutas de appi
]
