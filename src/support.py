import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

def comprobar_columnas(lista_df):
    """
    Comprueba si todos los DataFrames en una lista tienen las mismas columnas.

    Parámetros:
    ----------
    lista_df : list
        Lista que contiene los DataFrames a comparar.

    Retorna:
    -------
    bool
        Devuelve True si todos los DataFrames tienen las mismas columnas.
        Devuelve False si al menos uno de los DataFrames tiene columnas diferentes.

    """
    
    columnas_de_referencia = lista_df[0].columns
    for df in lista_df[1:]:
        if not columnas_de_referencia.equals(df.columns):
            return False
    return True

def rellenar_anios(lista_df, anios):
    """
    Rellena los valores faltantes en la columna 'ANO EXERCÍCIO' de cada DataFrame en la lista con el año correspondiente
    y convierte la columna a tipo entero.

    Args:
        lista_df (list): Lista de DataFrames.
        anios (list): Lista de años que se asignarán en caso de valores nulos.
    """
    for i, df in enumerate(lista_df):
        df['ANO EXERCÍCIO'].fillna(anios[i], inplace=True)
        df['ANO EXERCÍCIO'] = df['ANO EXERCÍCIO'].astype(int)

def convertir_a_float(columna):
    """
    Reemplaza las comas por puntos decimales en los valores de una columna y convierte la columna al tipo float.

    Parámetros:
    columna : pandas.Series
        La columna del DataFrame en la que se desea realizar la conversión.

    Returns:
    pandas.Series
        La columna con los valores convertidos a tipo float.
    """
    return columna.replace(',', '.', regex=True).astype(float)

# Definimos una función para rellenar nulos en las categorias relacionadas entre si
def completar_valores(df, col_codigo, col_nombre):
    
    # Creamos un diccionario de correspondencia entre las columnas especificadas
    df_sin_nulos=df.dropna(subset=[col_codigo, col_nombre])
    diccionario_correspondencias=df_sin_nulos.set_index(col_codigo)[col_nombre].to_dict()
    
    # Rellenamos los valores que faltan en ambas columnas
    df[col_nombre] = df[col_codigo].map(diccionario_correspondencias).combine_first(df[col_nombre])
    df[col_codigo] = df[col_nombre].map({v: k for k, v in diccionario_correspondencias.items()}).combine_first(df[col_codigo])
    
    return df

def eliminar_columnas(df, lista_columnas):
    """
    Elimina una lista de columnas de un DataFrame.

    Parámetros:
    ----------
    df : DataFrame
        El DataFrame del cual se eliminarán las columnas.
    lista_columnas : list
        Una lista con los nombres de las columnas que se eliminarán.

    Returns:
    --------
    DataFrame :
        El DataFrame sin las columnas especificadas.
    """
    columnas_a_eliminar = [col for col in lista_columnas if col in df.columns]
        
    df = df.drop(columns=columnas_a_eliminar)
    return df

def convertir_fecha(df, col_fecha):
    """
    Convierte una columna de fechas dadas en formato string a formato 'DD/MM/YYYY' para un DataFrame.
    
    Parámetros:
    df: DataFrame al que se aplicará la conversión.
    col_fecha: Nombre de la columna que contiene las fechas en formato string.
    
    Returns:
    DataFrame con la columna de fechas convertida.
    """
    # Convertimos la columna de fecha al formato datetime
    df[col_fecha] = pd.to_datetime(df[col_fecha], errors='coerce', dayfirst=True)
     
    return df

def mostrar_porcentaje_nulos(df):
    """
    Muestra un DataFrame con el porcentaje de valores nulos por columna, ordenado de mayor a menor.

    Parámetros:
    ----------
    df : DataFrame
        El DataFrame en del que se calcularán los porcentajes de valores nulos.

    Returns:
    --------
    DataFrame :
        Un DataFrame con el nombre de las columnas y su porcentaje de valores nulos, ordenado de mayor a menor.
    """
    porcentaje_nulos = df.isnull().mean() * 100
    df_nulos = porcentaje_nulos.reset_index()
    df_nulos.columns = ['COLUMNA', 'PORCENTAJE NULOS']
    df_nulos_ordenado = df_nulos.sort_values(by='PORCENTAJE NULOS', ascending=False)
    return df_nulos_ordenado

