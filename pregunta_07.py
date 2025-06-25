"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    # Se comienza creando un diccionario (vacío) para almacenar las letras por valor
    letras_por_valor = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo: # Abrir el archivo en modo lectura en la codificación utf-8
        for linea in archivo: # Iterar sobre cada línea del archivo
            columnas = linea.strip().split("\t") # Separar la línea en columnas usando tabulaciones como delimitador
            letra = columnas[0] # Tomar la primera columna (letra)
            valor = int(columnas[1]) # Convertir la segunda columna a entero (valor asociado)

            if valor in letras_por_valor: # Si el valor ya está en el diccionario, agregar la letra a la lista
                letras_por_valor[valor].append(letra)
            else: # Si el valor no está en el diccionario, crear una nueva entrada con una lista que contenga la letra
                letras_por_valor[valor] = [letra]

    resultado = sorted(letras_por_valor.items()) # Ordenar el diccionario por los valores (clave) y convertirlo a una lista de tuplas
    return resultado

resultado = pregunta_07()
print(resultado)  # Debe imprimir [(0, ['C']), (1, ['E', 'B', 'E']), (2, ['A', 'E']), (3, ['A', 'B', 'D', 'E', 'E', 'D']), (4, ['E', 'B']), (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']), (6, ['C', 'E', 'A', 'B']), (7, ['A', 'C', 'E', 'D']), (8, ['E', 'D', 'E', 'A', 'B']), (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

