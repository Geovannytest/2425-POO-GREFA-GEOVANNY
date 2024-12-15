class ClimaDiario:
    def __init__(self, dia, temperatura):
        self.dia = dia
        self.temperatura = temperatura

    def mostrar_informacion(self):
        print(f"Día: {self.dia}, Temperatura: {self.temperatura} °C")

class ClimaSemanal:
    def __init__(self):
        self.registros = []

    def agregar_clima_diario(self, clima_diario):
        self.registros.append(clima_diario)

    def calcular_promedio_temperaturas(self):
        if not self.registros:
            return 0
        suma_temperaturas = sum([registro.temperatura for registro in self.registros])
        return suma_temperaturas / len(self.registros)

    def mostrar_clima_semanal(self):
        print("Registro semanal de temperaturas:")
        for registro in self.registros:
            registro.mostrar_informacion()

# Programa principal
clima_semanal = ClimaSemanal()

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

print("Ingresa las temperaturas diarias:")
for dia in dias_semana:
    try:
        temperatura = float(input(f"Temperatura para {dia}: "))
        clima_diario = ClimaDiario(dia, temperatura)
        clima_semanal.agregar_clima_diario(clima_diario)
    except ValueError:
        print("Entrada no válida. Intenta nuevamente.")

print("\n--- Resumen semanal ---")
clima_semanal.mostrar_clima_semanal()
promedio = clima_semanal.calcular_promedio_temperaturas()
print(f"Promedio semanal de temperaturas: {promedio:.2f} °C")

promedio = clima_semanal.calcular_promedio_temperaturas()
print(f"Promedio semanal de temperaturas: {promedio:.2f} °C")
