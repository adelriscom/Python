from io import open

#Creacion del archivo, con OPEN se habre un flujo de datos que al final debe cerrarse. el parametro "w" me permite escribir. 
#archivo_externo=open("primerArchivo.txt", "w",)

#para agregar nuevo texto se debe usar el parametro "a"
#archivo_externo=open("primerArchivo.txt", "a")

#para leer el texto se debe usar el parametro "r"
archivo_externo=open("primerArchivo.txt", "r")

#se escribe texto en el archivo
#archivo_externo.write("\n Se guarda información permanente en el archivo desde el código python")

#para leer texto se usa el metodo read()
#informacion=archivo_externo.read()

#Para leer linea a linea se usa el metodo readLine()
informacion_Lineas=archivo_externo.readline()

#se cierra el flujo de datos
archivo_externo.close()

print(informacion_Lineas)