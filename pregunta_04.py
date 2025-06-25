"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    # Se comienza creando un diccionario (vacío) para contar los meses
    conteo_meses = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo: # Abrir el archivo en modo lectura en la codificación utf-8
        for linea in archivo: # Iterar sobre cada línea del archivo
            columnas = linea.strip().split("\t") # Separar la línea en columnas usando tabulaciones como delimitador
            fecha = columnas[2] # Tomar la tercera columna (fecha)
            mes = fecha.split("-")[1]  # extrae el mes en formato 'MM'
            if mes in conteo_meses: # Si el mes ya está en el diccionario, incrementar su conteo
                conteo_meses[mes] += 1
            else: # Si el mes no está en el diccionario, agregarlo con un conteo de 1
                conteo_meses[mes] = 1

    resultado = dict(sorted(conteo_meses.items())) # Ordenar el diccionario por los meses (clave) y convertirlo a una lista de tuplas
    return resultado

resultado = pregunta_04()
print(resultado)  

# Debe imprimir [('01', 3), ('02', 4), ('03', 2), ('04', 4), ('05', 3), ('06', 3), ('07', 5), ('08', 6), ('09', 3), ('10', 2), ('11', 2), ('12', 3)]