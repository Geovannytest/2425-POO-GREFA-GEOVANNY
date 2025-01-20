# Definición de Clase base
class Vehiculo:
    def __init__(self, marca, modelo):
        # Atributos públicos
        self.marca = marca
        self.modelo = modelo
        # Atributo privado
        self.__velocidad = 0

    # Método público
    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

    # Método para encapsulación (getter para __velocidad)
    def obtener_velocidad(self):
        return self.__velocidad

    # Método para encapsulación (setter para __velocidad)
    def establecer_velocidad(self, velocidad):
        if isinstance(velocidad, (int, float)) and velocidad >= 0:
            self.__velocidad = velocidad
        else:
            print("Velocidad no válida")

# Clase derivada que demuestra herencia
class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    # Sobrescritura de método (polimorfismo)
    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Tipo: {self.tipo}")

    # Método adicional en clase derivada
    def hacer_caballito(self):
        print(f"La moto {self.marca} {self.modelo} está haciendo un caballito!")

# Clase adicional que demuestra polimorfismo a través de métodos con diferentes argumentos
class MotocicletaDeportiva(Moto):
    def __init__(self, marca, modelo, tipo, cilindrada):
        super().__init__(marca, modelo, tipo)
        self.cilindrada = cilindrada

    # Sobrescritura de método (polimorfismo)
    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Tipo: {self.tipo}, Cilindrada: {self.cilindrada}cc")

    # Método que demuestra polimorfismo a través de argumentos variables
    def acelerar(self, *velocidades):
        for velocidad in velocidades:
            self.establecer_velocidad(velocidad)
            print(f"Acelerando a {velocidad} km/h")

# Creación de instancias y demostración de funcionalidadvehiculo = Vehiculo("Toyota", "Corolla")
vehiculo.mostrar_informacion()
vehiculo.establecer_velocidad(80)
print(f"Velocidad: {vehiculo.obtener_velocidad()} km/h")

moto = Moto("Yamaha", "MT-07", "Naked")
moto.mostrar_informacion()
moto.hacer_caballito()

moto_deportiva = MotocicletaDeportiva("Kawasaki", "Ninja H2", "Deportiva", 998)
moto_deportiva.mostrar_informacion()
moto_deportiva.acelerar(100, 150, 200)
