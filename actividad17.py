class inventario:
    def __init__(self):
        self.productos=[]
    def agregar_producto(self,producto):
        self.productos.append(producto)
        print(f"Producto: {producto} agregado al inventario")
