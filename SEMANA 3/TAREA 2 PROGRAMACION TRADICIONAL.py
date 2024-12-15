

def mostrar_clima_semanal(registros):
    print("Registro semanal de temperaturas:")
    for dia, temperatura in registros:
        print(f"Día: {dia}, Temperatura: {temperatura} °C")

def calcular_promedio_temperaturas(registros):
    if not registros:
        return 0
    suma_temperaturas = sum([temperatura for _, temperatura in registros])
    return suma_temperaturas / len(registros)

# Programa principal
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
registros = []

print("Ingresa las temperaturas diarias:")
for dia in dias_semana:
    try:
        temperatura = float(input(f"Temperatura para {dia}: "))
        registros.append((dia, temperatura))
    except ValueError:
        print("Entrada no válida. Intenta nuevamente.")

print("\n--- Resumen semanal ---")
mostrar_clima_semanal(registros)
promedio = calcular_promedio_temperaturas(registros)
print(f"Promedio semanal de temperaturas: {promedio:.2f} °C")
