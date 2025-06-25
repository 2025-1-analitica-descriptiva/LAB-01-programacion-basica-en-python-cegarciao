"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    #Se comienza creando un diccionario (vacío) para contar las letras
    conteo_letras = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo: # Abrir el archivo en modo lectura en la codificación utf-8
        for linea in archivo: # Iterar sobre cada línea del archivo
            columnas = linea.strip().split("\t") # Separar la línea en columnas usando tabulaciones como delimitador
            letra = columnas[0] # Tomar la primera columna (letra)
            if letra in conteo_letras: # Si la letra ya está en el diccionario, incrementar su conteo
                conteo_letras[letra] += 1
            else: # Si la letra no está en el diccionario, agregarla con un conteo de 1
                conteo_letras[letra] = 1

    resultado = sorted(conteo_letras.items()) # Ordenar el diccionario por las letras (clave) y convertirlo a una lista de tuplas
    return resultado

resultado = pregunta_02()
print(resultado)  # Debe imprimir [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]