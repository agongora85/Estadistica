#Definimos los módulos a importar
import pandas as pd
#Definimos las funciones a utilizar
from statistics import median,mean,mode,multimode
from math import isnan,floor
from itertools import filterfalse
#Definimos una serie simple numérica
serie=pd.Series([1,2,3])
print(serie)
#Definimos una serie de tipo cadena o texto
s = pd.Series(['Matemáticas', 'Historia', 'Economía', 'Programación', 'Inglés'], dtype='string')
print(s)
serie.name='nombre'
#Ordenación de la serie a nivel texto o cadena
print(sorted(s))
#Definimos una serie con columnas
df=pd.DataFrame({'Columna 1':[1,2,3,4],'Columna 2':['a','b','c','d']})
#Esto es una prueba para actualizar
print(df)
data=[20.7,15,63.25,142.14]
data2=[10,52,10,63,87,63,10,63]
print(sorted(data))
print(sorted(data,key=None,reverse=True))
print(median(data)) #Para obtener la mediana
print(sum(data)) #Obtener la sumatoria
print(floor(mean(data))) #Para obtener la media con rendondeo
print(mode(data2))
print(multimode(data2))
