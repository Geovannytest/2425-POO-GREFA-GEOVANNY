import json
import os


class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        return {"codigo": self.codigo, "nombre": self.nombre, "cantidad": self.cantidad, "precio": self.precio}


class Inventario:
    ARCHIVO = "inventario.txt"

    def __init__(self):
        self.productos = self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        try:
            with open(self.ARCHIVO, "w") as f:
                json.dump([p.to_dict() for p in self.productos], f)
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar en archivo: {e}")

    def cargar_desde_archivo(self):
        if not os.path.exists(self.ARCHIVO):
            return []
        try:
            with open(self.ARCHIVO, "r") as f:
                return [Producto(**p) for p in json.load(f)]
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Creando uno nuevo.")
            return []
        except json.JSONDecodeError:
            print("Error al leer el archivo: Formato corrupto. Se iniciará un inventario vacío.")
            return []
        except Exception as e:
            print(f"Error inesperado al cargar desde archivo: {e}")
            return []

    def agregar_producto(self, codigo, nombre, cantidad, precio):
        if any(p.codigo == codigo for p in self.productos):
            print("Error: El código del producto ya existe.")
            return
        self.productos.append(Producto(codigo, nombre, cantidad, precio))
        self.guardar_en_archivo()
        print("Producto agregado exitosamente.")

    def actualizar_producto(self, codigo, cantidad=None, precio=None):
        for p in self.productos:
            if p.codigo == codigo:
                if cantidad is not None:
                    p.cantidad = cantidad
                if precio is not None:
                    p.precio = precio
                self.guardar_en_archivo()
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def eliminar_producto(self, codigo):
        self.productos = [p for p in self.productos if p.codigo != codigo]
        self.guardar_en_archivo()
        print("Producto eliminado exitosamente.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        for p in self.productos:
            print(f"Código: {p.codigo}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")


# Interfaz de usuario
inventario = Inventario()

while True:
    print("\n1. Agregar Producto\n2. Actualizar Producto\n3. Eliminar Producto\n4. Mostrar Inventario\n5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
        inventario.agregar_producto(codigo, nombre, cantidad, precio)
    elif opcion == "2":
        codigo = input("Código del producto a actualizar: ")
        cantidad = input("Nueva cantidad (presione Enter para omitir): ")
        precio = input("Nuevo precio (presione Enter para omitir): ")
        cantidad = int(cantidad) if cantidad else None
        precio = float(precio) if precio else None
        inventario.actualizar_producto(codigo, cantidad, precio)
    elif opcion == "3":
        codigo = input("Código del producto a eliminar: ")
        inventario.eliminar_producto(codigo)
    elif opcion == "4":
        inventario.mostrar_inventario()
    elif opcion == "5":
        break
    else:
        print("Opción inválida.")
