import codecs
import sys
class MiArchivo:
#Constructor que recibirá el nombre del archivo que hace referencia a la dirección
    def __init__(self,nombre):
        """
        """
        self.nombre_archivo = nombre  #Inicializamos la variable 
        self.archivo = codecs.open(self.nombre_archivo, "r") #Abrimos el archivo y con "r " lo leemos

#Metodo retorna las lineas del archivo
    def obtener_informacion(self):
    	return self.archivo.readlines()
#Metodo cierra el archivo
    def cerrar_archivo(self):
        self.archivo.close()