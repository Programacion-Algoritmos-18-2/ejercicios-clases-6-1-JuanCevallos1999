class Busqueda(): #Creamos la clase Busqueda 
	def __init__(self, lista): #Constructor de la clase que recibe una lista ordenada 
		self.lista_ordenada = lista

	def setLista(self, lista): #Metodo para dar valores a la lista 
		self.lista_ordenada = lista

	def getLista(self):  #Metodo para obtener valores de la lista 
		return self.lista_ordenada
#Metodo que realiza el proceso de busqueda que recibe como parametro el elemento que se necesita
	def busquedaBinaria(self, elementoBusqueda): 
		elemento = elementoBusqueda #Recibimos el parametro en una variable 
		inferior = 0 #Variable que inicia en 0 por ser donde empieza la lista
		superior =  len(self.lista_ordenada) -1  #Superior hace referencia a el ultimo valor de la lista
		medio = int((inferior+superior+1)/2) #Medio es el valor intermedio de la lista
		ubicacion = -1 #La ubicación en donde se encuentre el elemento 
		while(inferior <= superior) and (ubicacion == -1): #While que se itera hasta que  retorne un valor par aubicacion
			if(elemento == self.lista_ordenada[medio]): #Comparacion para ver si se encontró el elemento
				ubicacion = medio #Actualización de la variable ubicacion
			elif(elemento < self.lista_ordenada[medio]): #Condición para evaluar y segmentar el segmento en donde se buscara el elemento
				superior = medio-1
			else:#Condición para evaluar y segmentar el segmento en donde se buscara el elemento
				inferior = medio+1 
			medio = int((inferior+superior+1)/2) 
		return ubicacion #Retorno de la posicion del elemento



