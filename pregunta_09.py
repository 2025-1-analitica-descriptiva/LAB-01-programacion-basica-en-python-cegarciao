"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    # Se comienza creando un diccionario (vacío) para contar las claves
    conteo_claves = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo: # Abrir el archivo en modo lectura en la codificación utf-8
        for linea in archivo: # Iterar sobre cada línea del archivo
            columnas = linea.strip().split("\t") # Separar la línea en columnas usando tabulaciones como delimitador
            
            if len(columnas) >= 5: # Asegurarse de que hay al menos cinco columnas
                pares_clave_valor_str = columnas[4] # Tomar la quinta columna (pares clave:valor)
                
                pares = pares_clave_valor_str.split(',') # Separar los pares clave:valor por comas
                
                for par in pares:
                    clave, _ = par.split(':') # Separar la clave y el valor usando el carácter `:` 
                    if clave in conteo_claves: # Si la clave ya está en el diccionario, incrementar su conteo
                        conteo_claves[clave] += 1
                    else: # Si la clave no está en el diccionario, agregarla con un conteo de 1
                        conteo_claves[clave] = 1
    
    return conteo_claves

resultado = pregunta_09()
print(resultado)  # Debe imprimir {'aaa': 13, 'bbb': 16, 'ccc': 23, 'ddd': 23, 'eee': 15, 'fff': 20, 'ggg': 13, 'hhh': 16, 'iii': 18, 'jjj': 18}