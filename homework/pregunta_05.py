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

def pregunta_05():
    valores = {}
    with open("files/input/data.csv", "r") as file:
        for line in file:
            partes = line.strip().split("\t")
            letra = partes[0]
            valor = int(partes[1])
            if letra in valores:
                valores[letra].append(valor)
            else:
                valores[letra] = [valor]
    
    resultado = []
    for letra in sorted(valores.keys()):
        maximo = max(valores[letra])
        minimo = min(valores[letra])
        resultado.append((letra, maximo, minimo))
    
    return resultado

print(pregunta_05())