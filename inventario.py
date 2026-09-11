# inicializar proyecto pystock

productos = []

def agregar_producto(nombre, cantidad, precio):
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor a cero")
    productos.append({
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    })