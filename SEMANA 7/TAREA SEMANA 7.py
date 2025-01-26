# Clase base Menu
class Menu:
    # Método constructor
    def __init__(self, platos, bebidas):
        self.platos = platos
        self.bebidas = bebidas

# Clase Desayuno heredada de Menu
class Desayuno(Menu):
    def __init__(self, platos, bebidas, frutas):
        super().__init__(platos, bebidas)
        self.frutas = frutas

    def mostrarInfo(self):
        print(f"Su desayuno es: {self.platos}")
        print(f"Su bebida seleccionada es: {self.bebidas}")
        print(f"Su fruta seleccionada es: {self.frutas}")

    def __del__(self):
        print("Destruyendo objeto Desayuno")

# Clase Almuerzo heredada de Menu
class Almuerzo(Menu):
    def __init__(self, platos, bebidas, postre):
        super().__init__(platos, bebidas)
        self.postre = postre

    def mostrarInfo(self):
        print(f"Su almuerzo es: {self.platos}")
        print(f"Su bebida seleccionada es: {self.bebidas}")
        print(f"Su postre seleccionado es: {self.postre}")

    def __del__(self):
        print("El objeto Almuerzo ha sido eliminado")

# Clase Merienda heredada de Menu
class Merienda(Menu):
    def __init__(self, platos, bebidas, postre):
        super().__init__(platos, bebidas)
        self.postre = postre

    def mostrarInfo(self):
        print(f"Su merienda es: {self.platos}")
        print(f"Su bebida seleccionada es: {self.bebidas}")
        print(f"Su postre seleccionado es: {self.postre}")

    def __del__(self):
        print("El objeto Merienda ha sido eliminado")


# Creación de instancias y prueba de las clases
# Desayuno
plato1 = Desayuno("continental", "jugo de mora", "papaya")
plato1.mostrarInfo()

# Almuerzo
plato2 = Almuerzo("encebollado", "jugo de limón", "flan")
plato2.mostrarInfo()

# Merienda
plato3 = Merienda("sándwich con pan integral", "yogur con granola", "crema de calabacín")
plato3.mostrarInfo()

# Eliminación manual de objetos (opcional, normalmente esto lo hace Python automáticamente)
del plato1
del plato2
del plato3
