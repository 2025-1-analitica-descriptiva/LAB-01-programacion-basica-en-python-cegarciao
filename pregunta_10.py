"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    # Se comienza creando una lista para almacenar los resultados
    resultados = []

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo: # Abrir el archivo en modo lectura en la codificación utf-8
        for linea in archivo: # Iterar sobre cada línea del archivo
            columnas = linea.strip().split("\t") # Separar la línea en columnas usando tabulaciones como delimitador
            
            if len(columnas) >= 5: # Asegurarse de que hay al menos cinco columnas
                letra_columna_0 = columnas[0] # Tomar la primera columna (letra)
                
                elementos_columna_3 = columnas[3].split(',') # Separar la cuarta columna por comas
                cantidad_elementos_columna_3 = len(elementos_columna_3)
                if elementos_columna_3 == ['']: # Verificar si la columna está vacía
                    cantidad_elementos_columna_3 = 0
                
                elementos_columna_4 = columnas[4].split(',') # Separar la quinta columna por comas
                cantidad_elementos_columna_4 = len(elementos_columna_4)
                if elementos_columna_4 == ['']: 
                    cantidad_elementos_columna_4 = 0
                
                resultados.append((letra_columna_0, cantidad_elementos_columna_3, cantidad_elementos_columna_4))
    
    return resultados