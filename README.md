# Punto de Venta Web - CRUD con Django

## Descripción del Proyecto

Este proyecto representa la implementación de un sistema CRUD en una aplicación web utilizando el patrón de diseño Modelo-Vista-Controlador (MVC) con Django. El objetivo principal ha sido desarrollar una aplicación web para un punto de venta, aplicando los conocimientos de Programación Orientada a Objetos (POO) en Python y utilizando HTML y CSS para la presentación visual.

## Funcionalidades

La aplicación web del Punto de Venta ofrece las siguientes funcionalidades:

- Menú interactivo para acceder fácilmente a las opciones.
- Operaciones de Crear, Leer, Actualizar y Eliminar para clientes, productos y facturas.
- Campos esenciales para productos: Nombre, Descripción, Precio y Stock.
- Campos esenciales para clientes: Nit, Nombre y Dirección.
- Modelo de factura con maestro y detalle para el almacenamiento de datos.
- Búsqueda y ordenamiento de productos, clientes y facturas.
- Templates HTML y estilos CSS para la visualización de datos.
- Uso de Django Models para definir la estructura de datos, Forms para la manipulación y Views para la lógica del negocio.
- Almacenamiento persistente mediante archivos XML.

## Estructura del Proyecto

- **models.py:** Definición de modelos utilizando Django Models para Clientes, Productos y Facturas.
- **forms.py:** Formularios para la creación y edición de datos.
- **views.py:** Lógica del negocio, implementación de CRUD y manejo de búsquedas y ordenamientos.
- **templates/:** Directorio que contiene los archivos HTML basados en el diseño MVC.
- **static/:** Directorio para archivos estáticos como CSS para la parametrización de estilos.

## Instrucciones de Ejecución

1. Clona el repositorio en tu máquina local.
2. Abre la terminal y navega al directorio del proyecto.
3. Ejecuta el servidor de Django con el comando `python manage.py runserver`.

**Nota:** Asegúrate de tener instalado Django en tu sistema.

## Colaborador Principal
- [Carbonell Castillo]

## Licencia
Este proyecto está bajo la licencia MIT.
