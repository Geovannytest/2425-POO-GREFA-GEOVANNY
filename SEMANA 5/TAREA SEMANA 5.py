# Conversor de Unidades de Longitud

def convertir_longitud(valor, unidad_origen, unidad_destino):
    """Convierte una longitud de una unidad a otra.

    Args:
        valor (float): La cantidad de longitud a convertir.
        unidad_origen (str): La unidad de origen ("metros", "kilometros", "millas", "pulgadas").
        unidad_destino (str): La unidad de destino ("metros", "kilometros", "millas", "pulgadas").

    Returns:
        float: El valor convertido a la unidad de destino.
    """
    # Diccionario de factores de conversión respecto a metros
    factores_conversion = {
        "metros": 1.0,
        "kilometros": 1000.0,
        "millas": 1609.34,
        "pulgadas": 0.0254
    }

    # Convertir el valor a metros
    valor_en_metros = valor * factores_conversion[unidad_origen]

    # Convertir de metros a la unidad de destino
    valor_convertido = valor_en_metros / factores_conversion[unidad_destino]

    return valor_convertido


def main():
    """Función principal del programa para manejar la entrada y salida del usuario."""
    print("Bienvenido al Conversor de Unidades de Longitud!")

    # Solicitar al usuario que ingrese el valor y las unidades
    valor = float(input("Ingrese el valor de la longitud: "))
    unidad_origen = input("Ingrese la unidad de origen (metros, kilometros, millas, pulgadas): ").lower()
    unidad_destino = input("Ingrese la unidad de destino (metros, kilometros, millas, pulgadas): ").lower()

    # Validar que las unidades ingresadas sean válidas
    unidades_validas = {"metros", "kilometros", "millas", "pulgadas"}
    if unidad_origen not in unidades_validas or unidad_destino not in unidades_validas:
        print("Unidades no válidas. Por favor, intente nuevamente.")
        return

    # Realizar la conversión
    resultado = convertir_longitud(valor, unidad_origen, unidad_destino)

    # Mostrar el resultado al usuario
    print(f"{valor} {unidad_origen} son equivalentes a {resultado:.2f} {unidad_destino}.")


if __name__ == "__main__":
    main()
