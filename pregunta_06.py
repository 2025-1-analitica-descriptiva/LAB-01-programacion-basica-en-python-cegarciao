"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
   # Se comienza creando un diccionario (vacío) para almacenar los valores por clave
    valores_por_clave = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo: # Abrir el archivo en modo lectura en la codificación utf-8
        for linea in archivo: # Iterar sobre cada línea del archivo
            columnas = linea.strip().split("\t") # Separar la línea en columnas usando tabulaciones como delimitador
            columna_5 = columnas[4].split(",") # Tomar la quinta columna y separarla por comas para obtener las claves y valores
            for par in columna_5: # Iterar sobre cada par clave:valor
                clave, valor = par.split(":") # Separar la clave y el valor usando el carácter `:`
                valor = int(valor) # Convertir el valor a entero
                if clave in valores_por_clave: # Si la clave ya está en el diccionario, agregar el valor a la lista
                    valores_por_clave[clave].append(valor)
                else: # Si la clave no está en el diccionario, crear una nueva entrada con una lista que contenga el valor
                    valores_por_clave[clave] = [valor]

    resultado = [] # Lista para almacenar los resultados finales
    for clave in sorted(valores_por_clave): # Iterar sobre las claves en orden alfabético
        lista_valores = valores_por_clave[clave] # Obtener la lista de valores para la clave actual
        minimo = min(lista_valores) # Calcular el valor mínimo de la lista
        maximo = max(lista_valores) # Calcular el valor máximo de la lista
        resultado.append((clave, minimo, maximo)) # Agregar una tupla con la clave, el mínimo y el máximo a la lista de resultados

    return resultado

resultado = pregunta_06()
print(resultado)  # Debe imprimir [('aaa', 1, 9), ('bbb', 1, 9), ('ccc', 1, 10), ('ddd', 0, 9), ('eee', 1, 7), ('fff', 0, 9), ('ggg', 3, 10), ('hhh', 0, 9), ('iii', 0, 9), ('jjj', 5, 17)]