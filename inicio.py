#Definimos los módulos a importar
import pandas as pd
#Definimos las funciones a utilizar
from statistics import median,mean,mode,multimode,fmean
from math import isnan,floor
#Definimos una serie simple numérica
serie=pd.Series([1,2,3])
print(serie)
print("La media es:"+str(median(serie)))
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
#---------- Trabajo con el archivo de Excel -----------------------
archivo1='data/Productividad.xlsx'
#Leemos el archivo de Excel
a=pd.read_excel(archivo1)
col=a.columns
#Obtenemos la lista de las columnas
col=col.tolist()
print(col)
#Imprimimos los valores por fila
valores=a.values
#Definimos las variables para obtener los datos estadísticos
sumpp=0
tpp=0
for columna in a:
    #print(a["Proyectos_planeados"])
    sumpp=a["Proyectos_planeados"]

print(sumpp)
for b in sumpp:
    tpp=tpp+b
#Se imprime los valores redondeados
print("La sumatoria de los proyectos planeados son:"+str(tpp))
print("La media de los proyectos planeados es:"+str((round(mean(sumpp),2))))
print("La sumatoria de los proyectos concretados es: "+str(sum(a["Proyectos concretados"])))
print("El empleado que tiene más movimientos es: "+str(mode(a["#Credencial"])))
print("Nivel de avance de todos los proyectos "+str(round((sum(a["Proyectos concretados"])/sum(a["Proyectos_planeados"]))*100))+"%")
# ------------------------------------------------------------
#---------------- Trabajo con listados ----------------------
data2=[20.7,15,63.25,142.14]
data3=[10,52,10,63,87,63,10,63]
data4=[5,float('NaN'),58,96,36,float('NaN'),74]

print(sorted(data2))
print(sorted(data2,key=None,reverse=True))
print(median(data3)) #Para obtener la mediana
print(sum(data3)) #Obtener la sumatoria
print(floor(mean(data3))) #Para obtener la media con rendondeo
print(mode(data3))
print(multimode(data3))
#La función map no sirve para encontrar todas aquellos valores que se encuentran perdidos
print(str(sum(map(isnan,data4))))
print("La media de los valores flotantes o decimales de data2 es:"+str(round(fmean(data2))))