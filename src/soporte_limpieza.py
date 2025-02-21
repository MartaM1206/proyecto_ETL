import pandas as pd

def trans_fecha(lista_col, dataframe):
    """
    Convierte las columnas especificadas de un DataFrame a tipo datetime.

    Parámetros:
    lista_col (list): Lista de nombres de columnas en el DataFrame que deben ser convertidas a tipo datetime.
    dataframe (pandas.DataFrame): El DataFrame que contiene las columnas a convertir.

    Retorna:
    pandas.DataFrame: El DataFrame con las columnas especificadas convertidas a tipo datetime. Los valores que no se pueden convertir se establecerán como NaT (Not a Time).
    """
    for col in lista_col:
        dataframe[col] = pd.to_datetime(dataframe[col], errors="coerce")
    return dataframe

def generar_mapa(col1, col2, dataframe):
    """
    Genera un diccionario a partir de los valores de dos columnas de un DataFrame, generando pares clave:valor por cada fila.

    Parámetros:
    col1 (str): Nombre de la primera columna que se usará como claves del diccionario.
    col2 (str): Nombre de la segunda columna que se usará como valores del diccionario.
    dataframe (pandas.DataFrame): El DataFrame que contiene las columnas a mapear.

    Retorna:
    dict: Un diccionario donde las claves son los valores de la columna col1 y los valores son los valores de la columna col2.
    """
    lista_col1 = []
    lista_col2 = []
    for i in dataframe[col1]:
        lista_col1.append(i)
    for f in dataframe[col2]:
        lista_col2.append(f)

    mapa = dict(zip(lista_col1, lista_col2))
    return mapa
