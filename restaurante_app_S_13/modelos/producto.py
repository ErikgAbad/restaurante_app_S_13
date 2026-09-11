class Producto:
    def __init__(self, id_producto, nombre, precio, categoria):
        self.id = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} ({self.categoria})"