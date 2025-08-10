class inventario:
    def __init__(self):
        self.productos=[]
    def agregar_producto(self,producto):
        self.productos.append(producto)
        print(f"Producto: {producto} agregado al inventario")
    def eliminar_producto(self,producto):
        if producto in self.productos:
            self.productos.remove(producto)
            print(f"El producto {producto} ha sido eliminado")
    def insertar_producto(self,posicion,producto):
        self.productos.insert(posicion,producto)
        print(f"Producto {producto} agregado en la posicion {posicion}")