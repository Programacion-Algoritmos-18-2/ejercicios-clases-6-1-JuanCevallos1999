from archivo.miarchivo import *  #Importamos las clases que usaremos 
from busqueda.Busqueda import *
elementoBuscar = 3 #Establecemos el elemento que vamos a buscar
mtxt = MiArchivo("data/datos.txt") #Enviamos la dirrección de archivo a la clase
lista = mtxt.obtener_informacion() #Obtenemos las lineas en una lista
lista = [l.split(",") for l in lista] #Hacemos un split para separar cada elemento seguido de una ","
lista2 = [] #Inicializamos una lista vacia que contendra los elementos ordenados
for d in lista: #For que recorre las lineas de la lista
	for numero in d:  #For que recorre cada elemento de cada linea
		e = int(numero) #Transformamos la cadena en entero 
		lista2.append(e) #Agregamos a la lista vacia los elementos como enteros 
lista2.sort() #Ordenamos la lista 
a = Busqueda(lista2) #Creamos un objeto y enviamos la lista ordenada a su constructor de clase
b = a.busquedaBinaria(3) #Creamos una variable que recibira el return del metodo busquedaBinaria 
if (b==-1):  #En caso de que no se enceuntre retorna -1 y presentamos el mensaje 
	print ("El número no existe")
else: #En caso de encontrare presentamos su posición
	print("La posicion es %s"%b)
mtxt.cerrar_archivo()