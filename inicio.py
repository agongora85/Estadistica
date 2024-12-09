import pandas as pd
import openpyxl
from statistics import median
from tabulate import tabulate
#Definimos una serie simple numérica
serie=pd.Series([1,2,3])
print(serie)
print("La media es:"+str(median(serie)))

#Definimos una serie de tipo cadena o texto
s = pd.Series(['Matemáticas', 'Historia', 'Economía', 'Programación', 'Inglés'], dtype='string')
print(s)
serie.name='nombre'
#Definimos una serie con columnas
df=pd.DataFrame({'Columna 1':[1,2,3,4],'Columna 2':['a','b','c','d']})
print(df)
#Obtenemos el tamaño de la tabla 
print(df.shape)
archivo='data/Resultados.xlsx'
excel_dataframe=openpyxl.load_workbook(archivo)
#Conocemos la hoja de calculo que se encuentra activa
print(excel_dataframe.active)
data_frame=excel_dataframe.active
data=[]
for row in range(1,data_frame.max_row):
    _row=[row]
    for col in data_frame.iter_cols(1,data_frame.max_column):
        #print(col[row].value)
        _row.append(col[row].value)
    data.append(_row)
headers=["Herramienta","Dominio del tema","Participación del grupo","Buena estructura","Claridad en contenido","Ejemplos","Tono de voz", "Tiempo de exposición","Imagenes"]
print(tabulate(data,headers=headers))