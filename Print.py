 # Tienda de Emilio - Registro de ventas de productos tecnológicos

Inventarios = {
    "LP01": {
        "articulo": "Laptop",
        "marcas": {
            "MacBook": 999.00,   
            "HP": 499.00,        
            "Dell": 529.00,      
        }
    },
    "MS01": {
        "articulo": "Mouse",
        "marcas": {
            "Logitech": 11.17,   
            "Razer": 29.90,      
            "HP": 14.90,         
        }
    },
    "TC01": {
        "articulo": "Teclado",
        "marcas": {
            "Logitech": 25.00, 
            "Redragon": 79.00, 
            "Corsair": 34.99,      
        }
    },
    "AU01": {
        "articulo": "Audifonos",
        "marcas": {
            "Sony": 44.90,     
            "JBL": 39.90,      
            "Apple": 189.00,    
        }
    },
    "CE01": {
        "articulo": "Celular",
        "marcas": {
            "Samsung": 135.00,   
            "iPhone": 869.00,    
            "Xiaomi": 199.00,  
        }
    }
}

# Lista donde se guardan los productos que el cliente va comprando
carrito = []

# Función para buscar cada producto en el diccionario de Inventarios
def buscar_producto(texto):
    texto = texto.strip().lower()
    for codigo, datos in Inventarios.items():
        if texto == codigo.lower() or texto == datos["articulo"].lower():
            return codigo
    return None
    
# Función para buscar la marca en el diccionario de cada producto 
def buscar_marca(texto, marcas):
    """Busca la marca por número de la lista (1, 2, 3) o por nombre. Devuelve la marca o None."""
    texto = texto.strip()
    lista_marcas = list(marcas.keys())

    if texto.isdigit():
        numero = int(texto)
        if 1 <= numero <= len(lista_marcas):
            return lista_marcas[numero - 1]
        return None

    for marca in lista_marcas:
        if texto.lower() == marca.lower():
            return marca
    return None

# Función para agregar los productos que compran los clientes en la lista del carrito
def agregar_al_carrito(articulo, marca, precio, cantidad):
    """Agrega un producto al carrito. Si ya estaba, solo le suma la cantidad."""
    for item in carrito:
        if item["articulo"] == articulo and item["marca"] == marca:
            item["cantidad"] += cantidad
            return
    carrito.append({
        "articulo": articulo,
        "marca": marca,
        "precio": precio,
        "cantidad": cantidad,
    })

# Función para registrar los productos que compra el cliente
def registrar_producto():
    """Pide producto, marca y cantidad. Devuelve True si se agregó al carrito."""
    # Mostrar los productos disponibles
    print("\nProductos disponibles:")
    for codigo, datos in Inventarios.items():
        print(f"  {codigo} - {datos['articulo']}")
    
    # Pedir el producto
    producto_texto = input("\nIngrese el producto que va a comprar el cliente: ")
    codigo = buscar_producto(producto_texto)
    if codigo is None:
        print("Ese producto no está en el inventario. Intente de nuevo.")
        return False
    
    # Definición de las variables: articulo y marcas
    articulo = Inventarios[codigo]["articulo"]
    marcas = Inventarios[codigo]["marcas"]
    
    # Mostrar las marcas con su precio
    print(f"\nMarcas disponibles de {articulo}:")
    numero = 1
    for marca, precio in marcas.items():
        print(f"  {numero}. {marca}: ${precio:,.2f}")
        numero += 1

    #Se solicitará por medio del codigo del producto la marca que desea el cajero 
    marca_texto = input("\n Seleccione la marca: ")
    marca = buscar_marca(marca_texto, marcas)
    if marca is None: 
        print("Esa marca no está disponible. Por favor, seleccione un codigo válido")
        return False 
    
    #Aqui el cajero ingresará la cantidad de articulos que se solicitó de esa marca selccionada 
    cantidad_texto = input("Ingrese la cantidad de articulos: ") .strip()
    if not cantidad_texto.isdigit() or int(cantidad_texto) <= 0:
        print("La cantidad debe ser un número entero mayor que 0. Intente de nuevo.")
        return False
    cantidad = int(cantidad_texto)
    
    #Sa agregó la función de agregar al carrito
    agregar_al_carrito(articulo, marca, marcas[marca], cantidad)
    subtotal = marcas[marca] * cantidad
    print(f"\nAgregado: { cantidad} x {articulo} {marca} = ${subtotal:,.2f}")
    return True 

#Esta funcion es para imprimir el ticket final cuando se hayan agregado al carrito todos los articulos
def imprimir_ticket(): 
    "Imprime el ticket final con todos los productos del carrito y el total."
    print("---Tienda de Emilio---")
    print("--Ticket final--")
    
    total = 0
    for item in carrito: 
        subtotal = item["precio"] * item["cantidad"] 
        total += subtotal
        print(f"\n Producto: {item['articulo']} {item['marca']}")    
        
    print(f"Total a pagar: $ {total:,.2f}")
    print("---Gracias por su compra---")