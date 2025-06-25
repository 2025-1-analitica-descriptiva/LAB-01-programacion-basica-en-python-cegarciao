"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    # Se comienza creando un diccionario para almacenar las letras únicas por valor
    letras_unicas_por_valor = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo: # Abrir el archivo en modo lectura en la codificación utf-8
        for linea in archivo: # Iterar sobre cada línea del archivo
            columnas = linea.strip().split("\t") # Separar la línea en columnas usando tabulaciones como delimitador
            
            if len(columnas) >= 2: # Asegurarse de que hay al menos dos columnas
                letra_columna_0 = columnas[0] # Tomar la primera columna (letra)
                valor_columna_1 = int(columnas[1]) # Tomar la segunda columna (valor) y convertirla a entero

                if valor_columna_1 not in letras_unicas_por_valor:  # Si el valor no está en el diccionario, inicializar un conjunto vacío
                    letras_unicas_por_valor[valor_columna_1] = set()
                
                letras_unicas_por_valor[valor_columna_1].add(letra_columna_0) # Agregar la letra al conjunto correspondiente al valor

    resultado_final = []  # Lista para almacenar el resultado final como tuplas
    for valor in sorted(letras_unicas_por_valor.keys()): # Iterar sobre los valores en orden ascendente
        lista_letras_ordenadas = sorted(list(letras_unicas_por_valor[valor])) # Convertir el conjunto de letras a una lista y ordenarla
        resultado_final.append((valor, lista_letras_ordenadas)) # Agregar una tupla con el valor y la lista de letras ordenadas a la lista de resultados
    
    return resultado_final

resultado = pregunta_08()
print(resultado)  # Debe imprimir [(0, ['C']), (1, ['B', 'E']), (2, ['A', 'E']), (3, ['A', 'B', 'D', 'E']), (4, ['B', 'E']), (5, ['B', 'C', 'D', 'E']), (6, ['A', 'B', 'C', 'E']), (7, ['A', 'C', 'D', 'E']), (8, ['A', 'B', 'D', 'E']), (9, ['A', 'B', 'C', 'E'])]