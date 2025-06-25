"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    # Se comienza creando un diccionario (vacío) para almacenar los valores por letra
    valores_por_letra = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo: # Abrir el archivo en modo lectura en la codificación utf-8
        for linea in archivo: # Iterar sobre cada línea del archivo
            columnas = linea.strip().split("\t") # Separar la línea en columnas usando tabulaciones como delimitador
            letra = columnas[0] # Tomar la primera columna (letra)
            valor = int(columnas[1]) # Tomar la segunda columna (valor) y convertirla a entero

            if letra in valores_por_letra: # Si la letra ya está en el diccionario, agregar el valor a la lista
                valores_por_letra[letra].append(valor)
            else: # Si la letra no está en el diccionario, crear una nueva entrada con una lista que contenga el valor
                valores_por_letra[letra] = [valor]

    resultado = [] # Lista para almacenar los resultados finales
    for letra in sorted(valores_por_letra): # Iterar sobre las letras en orden alfabético
        lista_valores = valores_por_letra[letra] # Obtener la lista de valores para la letra actual
        maximo = max(lista_valores) # Calcular el valor máximo de la lista
        minimo = min(lista_valores) # Calcular el valor mínimo de la lista
        resultado.append((letra, maximo, minimo)) # Agregar una tupla con la letra, el máximo y el mínimo a la lista de resultados

    return resultado

resultado = pregunta_05()
print(resultado)  # Debe imprimir [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]