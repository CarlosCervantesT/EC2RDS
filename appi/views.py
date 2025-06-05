from django.shortcuts import render 
import xml.etree.ElementTree as ET
import xml.dom.minidom



def home(request):
    if request.method == "POST":
        saludo = request.POST.get("saludo")
        print(saludo)
        return render(request, "pagina.html",{"SALUDO":saludo})
    
    return render(request, 'dashboard.html')

def mas_vendidos(request):
    productos = leer_xml("producto.xml")
    total_productos = len(productos)
    print(total_productos)
    return render(request, "masVendidos.html", {"productos": productos, "total_productos": total_productos})

def listar_topClientes(request):
    clientes = leer_xml("cliente.xml")
    total_clientes = len(clientes)
    print(total_clientes)
    return render(request, "topClientes.html", {"clientes": clientes, "total_clientes": total_clientes})

def registrarCliente(request):
    cliente = ""
    if request.method == "POST":
        nuevo_cliente={
            "nit":request.POST.get("nit"),
            "nombre":request.POST.get("nombre"),
            "direccion":request.POST.get("direccion")
        }

        clientes = leer_xml("cliente.xml")
        clientes.append(nuevo_cliente)
        escribir_xml("cliente.xml", clientes)

        cliente = request.POST.get("nit")
        ##mensaje en pantalla que se registro correctamente
        mensaje = "Registro exitoso"
        return render(request, "registroClientes.html", {"cliente": cliente})
    
        # Realiza cualquier lógica adicional aquí, por ejemplo, guardar el cliente en la base de datos.
        # return render(request, "registroClientes.html", {"cliente": cliente})

    # Si es una solicitud GET, simplemente renderiza el formulario.
    return render(request, "registroClientes.html")
    
def editar_cliente(request):
    cliente = ""
    if request.method == "POST":
        cliente_id = request.POST.get("cliente_id")
        nuevo_nombre = request.POST.get("nombre")
        nuevo_direccion = request.POST.get("direccion")


        clientes = leer_xml("cliente.xml")
        cliente_editar = next((cliente for cliente in clientes if cliente.get('nit') == cliente_id), None)

        if cliente_editar:
            if nuevo_nombre:
                cliente_editar['nombre'] = nuevo_nombre
            if nuevo_direccion:
                cliente_editar['direccion'] = nuevo_direccion
            
            escribir_xml("cliente.xml", clientes)
        clientes = leer_xml("cliente.xml")
        return render(request, "editarCliente.html", {"cliente": cliente, "clientes": clientes})
    
    else:
        clientes = leer_xml("cliente.xml")
        for cliente in clientes:
            print(cliente.get("nit"))

        return render(request, "editarCliente.html", {"clientes": clientes})
    
def eliminar_cliente(request):
    cliente = ""
    if request.method == "POST":
        cliente_id = request.POST.get("cliente_id")

        clientes = leer_xml("cliente.xml")
        clientes = [cliente for cliente in clientes if cliente.get('nit') != cliente_id]

        escribir_xml("cliente.xml", clientes)
        clientes = leer_xml("cliente.xml")
        return render(request, "eliminarCliente.html", {"cliente": cliente, "clientes": clientes})
    else:
        clientes = leer_xml("cliente.xml")
        for cliente in clientes:
            print(cliente.get("nit"))

        return render(request, "eliminarCliente.html", {"clientes": clientes})

def listar_clientes(request):
    clientes = leer_xml("cliente.xml")
    total_clientes = len(clientes)
    print(total_clientes)
    return render(request, "listarClientes.html", {"clientes": clientes, "total_clientes": total_clientes})



##funciones de productos
def registrar_producto(request):
    producto = ""
    if request.method == "POST":
        nuevo_producto={
            "nombre":request.POST.get("nombre"),
            "precio":request.POST.get("precio"),
            "stock":request.POST.get("stock"), ##stock es la cantidad de productos que hay en existencia
            "descripcion":request.POST.get("descripcion")
        }

        productos = leer_xml("producto.xml")
        productos.append(nuevo_producto)
        escribir_xml('producto.xml', productos, root_name="productos", item_name="producto")
        ##mensaje en pantalla que se registro correctamente
        mensaje = "Registro exitoso"
        return render(request, "registroProductos.html", {"producto": producto})
    
        # Realiza cualquier lógica adicional aquí, por ejemplo, guardar el cliente en la base de datos.
        # return render(request, "registroClientes.html", {"cliente": cliente})

    # Si es una solicitud GET, simplemente renderiza el formulario.
    return render(request, "registroProductos.html")

def editar_producto(request):
    producto = ""
    if request.method == "POST":
        producto_id = request.POST.get("producto_id")
        nuevo_nombre = request.POST.get("nombre")
        nuevo_precio = request.POST.get("precio")
        nuevo_descripcion = request.POST.get("descripcion")
        nuevo_stock = request.POST.get("stock")


        productos = leer_xml("producto.xml")
        producto_editar = next((producto for producto in productos if producto.get('nombre') == producto_id), None)

        if producto_editar:
            if nuevo_nombre:
                producto_editar['nombre'] = nuevo_nombre
            if nuevo_precio:
                producto_editar['precio'] = nuevo_precio
            if nuevo_descripcion:
                producto_editar['descripcion'] = nuevo_descripcion
            if nuevo_stock:
                producto_editar['stock'] = nuevo_stock
            
            escribir_xml("producto.xml", productos)
        productos = leer_xml("producto.xml")
        return render(request, "editarProducto.html", {"producto": producto, "productos": productos})
    
    else:
        productos = leer_xml("producto.xml")
        for producto in productos:
            print(producto.get("nombre"))

        return render(request, "editarProducto.html", {"productos": productos})

def eliminar_producto(request):
    producto = ""
    if request.method == "POST":
        producto_id = request.POST.get("producto_id")

        productos = leer_xml("producto.xml")
        productos = [producto for producto in productos if producto.get('nombre') != producto_id]

        escribir_xml("producto.xml", productos)
        productos = leer_xml("producto.xml")
        return render(request, "eliminarProducto.html", {"producto": producto, "productos": productos})
    else:
        productos = leer_xml("producto.xml")
        for producto in productos:
            print(producto.get("nombre"))

        return render(request, "eliminarProducto.html", {"productos": productos})

def listar_productos(request):
    productos = leer_xml("producto.xml")
    total_productos = len(productos)
    print(total_productos)
    return render(request, "listarProductos.html", {"productos": productos, "total_productos": total_productos})

##Funciones para facturas
# def registrar_factura(request):
#     if request.method == "POST":
#         factura = request.POST.getlist("factura")
#         mensaje = "Registro exitoso"
#         print("entro")
#         print(factura)
#         return render(request, "factura.html", {"factura": factura, "mensaje": mensaje})

#     return render(request, "factura.html")


def registrar_factura(request):
    factura = ""
    if request.method == "POST":
        cliente_id = request.POST.get("cliente_id")
        ##obtenemos los datos del cliente
        clientes = leer_xml("cliente.xml")
        print(clientes)
        cliente = next((cliente for cliente in clientes if cliente.get('nit') == cliente_id), None)
        ##imprimimos los datos del cliente
        print("Datos del cliente")
        print(cliente.get("nit"))
        print(cliente.get("nombre"))
        print(cliente.get("direccion"))
        clientesObtenidos = []
        datos_cliente = {
            "nit": cliente.get("nit"),
            "nombre": cliente.get("nombre"),
            "direccion": cliente.get("direccion")
        }
        clientesObtenidos.append(datos_cliente)
        ##obtenemos los datos de los productos
        productosObtenidos = request.POST.getlist("productos")
        almacenProductos = []
        productos = leer_xml("producto.xml")
        productos = [producto for producto in productos if producto.get('nombre') in productosObtenidos]
        for producto in productos:
            print(producto.get("nombre"))
            print(producto.get("precio"))
            print(producto.get("stock"))
            print(producto.get("descripcion"))
            producto_procesar = {
                "nombre": producto.get("nombre"),
                "precio": producto.get("precio"),
                "stock": producto.get("stock"),
                "descripcion": producto.get("descripcion")
            }
            almacenProductos.append(producto_procesar)
        ##imprimimos los datos de los productos
            print("Datos de los productos")
            print(almacenProductos)

                
        print("22Datos de los productos222")
        print(productos)

        facturas= leerXMLFactura("factura.xml")
        if facturas:
            numero = int(facturas[-1][0]) + 1
        else:
            numero = 1
        facturas.append([str(numero), clientesObtenidos, almacenProductos])
        generar_xml_factura("factura.xml", facturas)
        
        print("*"*27)
        print(facturas)
        ##imprimimos los datos de los productos


        
        ##mensaje en pantalla que se registro correctamente
        mensaje = "Registro exitoso"
        
        clientes = leer_xml("cliente.xml")
        return render(request, "registrarFactura.html", {"producto": producto, "productos": productos, "factura": factura, "clientes": clientes})
    
    else:
        clientes = leer_xml("cliente.xml")
        productos = leer_xml("producto.xml")
        for cliente in clientes:
            print(cliente.get("nit"))

        return render(request, "registrarFactura.html", {"clientes": clientes, "productos": productos, "factura": None})
        # Realiza cualquier lógica adicional aquí, por ejemplo, guardar el cliente en la base de datos.
        # return render(request, "registroClientes.html", {"cliente": cliente})

def listar_facturas(request):
    facturas = leerXMLFactura("factura.xml")
    total_facturas = len(facturas)
    print(total_facturas)
    print(facturas)
    return render(request, "listarFacturas.html", {"facturas": facturas, "total_facturas": total_facturas})
    
def editar_factura(request):
    factura = ""
    if request.method == "POST":
        print("Entro a edaitar factura")
        factura_id = request.POST.get("factura_id")
        cliente_id = request.POST.get("cliente_id")
        clientes_obtenidos = []
        ##obtenemos los datos del cliente
        clientes = leer_xml("cliente.xml")
        print("Imprime los clientes obtenidos")
        print(clientes)

        cliente = next((cliente for cliente in clientes if cliente.get('nit') == cliente_id), None)
        ##imprimimos los datos del cliente
        nuevo_cliente = {
            "nit": cliente.get("nit"),
            "nombre": cliente.get("nombre"),
            "direccion": cliente.get("direccion")
        }
        print("Imprime el cliente obtenido")
        print(nuevo_cliente)

        clientes_obtenidos.append(nuevo_cliente)
        ##obtenemos los datos de los productos
        productosObtenidos = request.POST.getlist("productos")
        almacenProductos = []

        productos = leer_xml("producto.xml")
        productos = [producto for producto in productos if producto.get('nombre') in productosObtenidos]
        for producto in productos:
            print(producto.get("nombre"))
            print(producto.get("precio"))
            print(producto.get("stock"))
            print(producto.get("descripcion"))
            producto_procesar = {
                "nombre": producto.get("nombre"),
                "precio": producto.get("precio"),
                "stock": producto.get("stock"),
                "descripcion": producto.get("descripcion")
            }
            almacenProductos.append(producto_procesar)
        ##imprimimos los datos de los productos
            print("Datos de los productos")
            print(almacenProductos)

        
        facturas = leerXMLFactura("factura.xml")
        facturas_editar = next((factura for factura in facturas if factura[0] == factura_id), None)
        print("entrooooooooooo")
        if facturas_editar:
            facturas_editar[1] = clientes_obtenidos
            facturas_editar[2] = almacenProductos
            generar_xml_factura("factura.xml", facturas)
        #editamos la factura

        facturas = leerXMLFactura("factura.xml")
        clientes = leer_xml("cliente.xml")
        return render(request, "editarFactura.html", {"producto": producto, "productos": productos, "factura2": factura, "facturas": facturas, "clientes": clientes})
    
    else:
        facturas = leerXMLFactura("factura.xml")
        clientes = leer_xml("cliente.xml")
        productos = leer_xml("producto.xml")
        #impirmir numero de factura
        
        for cliente in clientes:
            print(cliente.get("nit"))

        return render(request, "editarFactura.html", {"clientes": clientes, "productos": productos, "factura2": None, "facturas": facturas})

def eliminar_factura(request):
    factura = ""
    if request.method == "POST":
        factura_id = request.POST.get("factura_id")

        facturas = leerXMLFactura("factura.xml")
        facturas = [factura for factura in facturas if factura[0] != factura_id]

        generar_xml_factura("factura.xml", facturas)
        facturas = leerXMLFactura("factura.xml")
        return render(request, "eliminarFactura.html", {"factura": factura, "facturas": facturas})
    else:
        facturas = leerXMLFactura("factura.xml")
        for factura in facturas:
            print(factura[0])

        return render(request, "eliminarFactura.html", {"facturas": facturas, "factura": None})
    

def leer_xml(ruta_archivo):
    try:
        tree = ET.parse(ruta_archivo)
        root = tree.getroot()
        datos = []
        for elemento in root:
            item = {}
            for hijo in elemento:
                item[hijo.tag] = hijo.text
            
            if item:
                datos.append(item)
        return datos
    except FileNotFoundError:
        
        return []
    

def leerXMLFactura(xml_file):
    try:
        tree = ET.parse(xml_file)
    
        root = tree.getroot()

        facturas = []
        productosObtenidos = []
        clientesObtenidos = []
        for factura in root.findall('factura'):
            clientesObtenidos = []
            productosObtenidos = []
            numero = factura.find('numero').text
            print(numero)
            for cliente in factura.findall('cliente'):
                nit = cliente.find('nit').text
                nombre = cliente.find('nombre').text
                direccion = cliente.find('direccion').text
                # print(nit, nombre, direccion)
                clientesObtenido = {
                    "nit": nit,
                    "nombre": nombre,
                    "direccion": direccion
                }
                clientesObtenidos.append(clientesObtenido)
            for productos in factura.findall('productos'):
                
                for producto in productos.findall('producto'):
                    
                    nombre = producto.find('nombre').text
                    precio = producto.find('precio').text
                    stock = producto.find('stock').text
                    descripcion = producto.find('descripcion').text
                    productosObtenido = {
                        "nombre": nombre,
                        "precio": precio,
                        "stock": stock,
                        "descripcion": descripcion
                    }
                    productosObtenidos.append(productosObtenido)
                
            
                    # print(nombre, precio, stock)
            facturas.append([numero, clientesObtenidos, productosObtenidos])
        return facturas
    except FileNotFoundError:
        
        return []
    
        

# FUNCION ESCRIBIR DATOS XML
def escribir_xml(ruta_archivo, datos, root_name="data", item_name="item"):
    root = ET.Element(root_name)
    for item in datos:
        elemento = ET.SubElement(root, item_name)
        for clave, valor in item.items():
            ET.SubElement(elemento, clave).text = valor
    tree = ET.ElementTree(root)
    
    with open(ruta_archivo, "wb") as ruta_archivo:
        print("entro a escribir")
        tree.write(ruta_archivo, encoding="utf-8", xml_declaration=True, method="xml")
        indent_xml_file(ruta_archivo)

def generar_xml_factura(xml_file, facturas):
    root = ET.Element("facturas")
    for factura in facturas:
        factura_xml = ET.SubElement(root, "factura")
        numero = ET.SubElement(factura_xml, "numero")
        numero.text = factura[0]
        cliente = ET.SubElement(factura_xml, "cliente")
        nit = ET.SubElement(cliente, "nit")
        nit.text = factura[1][0]["nit"]
        nombre = ET.SubElement(cliente, "nombre")
        nombre.text = factura[1][0]["nombre"]
        direccion = ET.SubElement(cliente, "direccion")
        direccion.text = factura[1][0]["direccion"]
        productos = ET.SubElement(factura_xml, "productos")
        for producto in factura[2]:
            producto_xml = ET.SubElement(productos, "producto")
            nombre = ET.SubElement(producto_xml, "nombre")
            nombre.text = producto["nombre"]
            precio = ET.SubElement(producto_xml, "precio")
            precio.text = producto["precio"]
            stock = ET.SubElement(producto_xml, "stock")
            stock.text = producto["stock"]
            descripcion = ET.SubElement(producto_xml, "descripcion")
            descripcion.text = producto["descripcion"]
    tree = ET.ElementTree(root)
    with open("factura.xml", "wb") as xml_file:
        print("entro a escribir")
        tree.write(xml_file, encoding="utf-8", xml_declaration=True, method="xml")
        indent_xml_file(xml_file)
    print("entro a escribir")

def indent_xml_file(xml_file):

    with open(xml_file.name, "rb") as f:
        content = f.read()


    dom = xml.dom.minidom.parseString(content)
    indented_content = dom.toprettyxml(encoding="utf-8")


    with open(xml_file.name, "wb") as f:
        f.write(indented_content)