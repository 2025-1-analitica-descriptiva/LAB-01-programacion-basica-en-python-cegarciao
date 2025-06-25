"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    # Se comienza creando un diccionario (vacío) para almacenar la suma por letra
    suma_por_letra = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo: # Abrir el archivo en modo lectura en la codificación utf-8
        for linea in archivo: # Iterar sobre cada línea del archivo
            columnas = linea.strip().split("\t") # Separar la línea en columnas usando tabulaciones como delimitador
            letra = columnas[0] # Tomar la primera columna (letra)
            valor = int(columnas[1]) # Convertir la segunda columna a entero (valor a sumar)
            if letra in suma_por_letra: # Si la letra ya está en el diccionario, sumar el valor
                suma_por_letra[letra] += valor
            else: # Si la letra no está en el diccionario, agregarla con el valor actual
                suma_por_letra[letra] = valor

    resultado = sorted(suma_por_letra.items()) # Ordenar el diccionario por las letras (clave) y convertirlo a una lista de tuplas
    return resultado

resultado = pregunta_03()
print(resultado)  # Debe imprimir [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]