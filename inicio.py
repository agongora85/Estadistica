import pandas as pd
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