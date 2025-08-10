class Inventario:
    def __init__(self):
        self.productos=[]
    def agregar_producto(self,producto):
        self.productos.append(producto)
        print(f"Producto: {producto} agregado al inventario")
    def eliminar_producto(self,producto):
        if producto in self.productos:
            self.productos.remove(producto)
            print(f"El producto {producto} ha sido eliminado")
        else:
            print("Producto no encontrado")
    def insertar_producto(self,posicion,producto):
        self.productos.insert(posicion,producto)
        print(f"Producto {producto} agregado en la posicion {posicion}")
    def ordenar_productos(self):
        self.productos.sort()
        print("Productos ordenados alfabeticamente")
    def mostar_productos(self):
        if not self.productos:
            print("Inventario vacio")
        else:
            print("Inventario:")
            for i in self.productos:
                print(f"-{i}")
    def buscar_producto(self,producto):
        if producto in self.productos:
            posicion= self.productos.index(producto)
            print(f"Producto {producto} esta en la posicion {posicion}")
        else:
            print("Producto no encontrado")
    def vaciar_inventario(self):
        self.productos.clear()
        print("Inventario vaciado")
inventario= Inventario()
while True:
    print("Menu")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Agregar producto en una posicion")
    print("4. Ordenar productos")
    print("5. Mostrar productos")
    print("6. Buscar un producto")
    print("7. Vaciar inventario")
    print("8. Salir")
    opcion= input("Ingrese una de las opciones: ")
    match opcion:
        case "1":
            while True:
                producto= input("Ingrese el producto a agregar: ")
                inventario.agregar_producto(producto)
                if not producto:
                    print("El producto no puede estar vacio")
                else:
                    break
        case "2":
            while True:
                producto = input("Ingrese el producto a eliminar: ")
                inventario.eliminar_producto(producto)
                if not producto:
                    print("Ingrese un producto")
                else:
                    break
        case "3":
            try:
                posicion =int(input("Ingrese la posicion: "))
                while True:
                    producto =input("Ingrese el producto a agregar en la posicion: ")
                    inventario.insertar_producto(posicion,producto)
                    if not producto:
                        print("Ingrese un producto")
                    else:
                        break
            except ValueError:
                print("La posicion debe ser un numero entero")
            except Exception as e:
                print("Error al agregar producto: ",e)
        case "4":
            inventario.ordenar_productos()
        case "5":
            inventario.mostar_productos()
        case "6":
            producto= input("Ingrese el producto a buscar: ")
            inventario.buscar_producto(producto)
        case "7":
            inventario.vaciar_inventario()
        case "8":
            print("Saliendo del programa...")
            break
        case _:
            print("Error: ingrese una de las opciones")