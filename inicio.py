#Definimos los módulos a importar
import pandas as pd
#Definimos las funciones a utilizar
from statistics import median,mean
from math import isnan
from itertools import filterfalse
#Definimos una serie simple numérica
serie=pd.Series([1,2,3])
print(serie)
#Definimos una serie de tipo cadena o texto
s = pd.Series(['Matemáticas', 'Historia', 'Economía', 'Programación', 'Inglés'], dtype='string')
print(s)
serie.name='nombre'
#Definimos una serie con columnas
df=pd.DataFrame({'Columna 1':[1,2,3,4],'Columna 2':['a','b','c','d']})
#Esto es una prueba para actualizar
print(df)
data=[20.7,15,63.25,142.14]
print(sorted(data))
print(sorted(data,key=None,reverse=True))
print(median(data)) #Para obtener la mediana
print(sum(data)) #Obtener la sumatoria
print(mean(data))