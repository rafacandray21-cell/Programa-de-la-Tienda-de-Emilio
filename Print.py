#Dejo este comentario para comprobar que se haya subido exitosamente este archivo a Github. 

#Hago este comentario para ver si se actualiza dentro de VSCODE 

# Tienda de Emilio - Registro de ventas de productos tecnológicos

Inventarios = {
    "LP01": {
        "articulo": "Laptop",
        "marcas": {
            "MacBook": 999.00,   # MacBook Air 
            "HP": 499.00,        # HP 15 
            "Dell": 529.00,      # Dell Inspiron 3520
        }
    },
    "MS01": {
        "articulo": "Mouse",
        "marcas": {
            "Logitech": 11.17,   # Mouse inalámbrico Logitech 
            "Razer": 29.90,      # Mouse gaming Razer 
            "HP": 14.90,         # Mouse óptico inalámbrico HP 
        }
    },
    "TC01": {
        "articulo": "Teclado",
        "marcas": {
            "Logitech": 25.00,   # Teclado inalámbrico Logitech 
            "Redragon": 79.00,   # Kit teclado + mouse Redragon
            "Corsair": 34.99,    # Teclado Corsair    
        }
    },
    "AU01": {
        "articulo": "Audifonos",
        "marcas": {
            "Sony": 44.90,       # Audífonos Bluetooth Sony 
            "JBL": 39.90,        # Audífonos inalámbricos JBL
            "Apple": 189.00,     # Apple AirPods 
        }
    },
    "CE01": {
        "articulo": "Celular",
        "marcas": {
            "Samsung": 135.00,   # Samsung Galaxy 
            "iPhone": 869.00,    # iPhone 16e
            "Xiaomi": 199.00,    # Xiaomi Redmi 
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
