from django.contrib import admin
from django.urls import path
from appi import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),  # Ruta para la página principal
]
