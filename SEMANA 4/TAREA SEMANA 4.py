#  Sistema de Reservas de Hotel

class Habitacion:
    """Clase que representa una habitación en un hotel."""
    def __init__(self, numero, tipo, precio):
        self.numero = numero  # Número de la habitación
        self.tipo = tipo  # Tipo de habitación (simple, doble, suite)
        self.precio = precio  # Precio por noche
        self.disponible = True  # Disponibilidad de la habitación

    def reservar(self):
        """Marca la habitación como reservada."""
        if self.disponible:
            self.disponible = False
            return True
        return False

    def liberar(self):
        """Marca la habitación como disponible."""
        self.disponible = True


class Cliente:
    """Clase que representa un cliente del hotel."""
    def __init__(self, nombre, identificacion):
        self.nombre = nombre  # Nombre del cliente
        self.identificacion = identificacion  # Identificación del cliente


class Reserva:
    """Clase que representa una reserva en el hotel."""
    def __init__(self, cliente, habitacion, noches):
        self.cliente = cliente  # Cliente que realiza la reserva
        self.habitacion = habitacion  # Habitación reservada
        self.noches = noches  # Número de noches de la reserva

    def costo_total(self):
        """Calcula el costo total de la reserva."""
        return self.noches * self.habitacion.precio


# Ejemplo de uso
if __name__ == "__main__":
    # Crear habitaciones
    habitacion1 = Habitacion(101, "Simple", 50)
    habitacion2 = Habitacion(102, "Doble", 80)
    habitacion3 = Habitacion(103, "Suite", 120)

    # Crear cliente
    cliente1 = Cliente("Geovanny Grefa", "1500735269")

    # Realizar reserva
    if habitacion1.reservar():
        reserva1 = Reserva(cliente1, habitacion1, 2)
        print(f"Reserva exitosa para {reserva1.cliente.nombre} en la habitación {reserva1.habitacion.numero} por {reserva1.noches} noches.")
        print(f"Costo total: ${reserva1.costo_total()}")
    else:
        print("La habitación no está disponible.")

    # Liberar habitación
    habitacion1.liberar()
    print(f"La habitación {habitacion1.numero} está ahora disponible.")
