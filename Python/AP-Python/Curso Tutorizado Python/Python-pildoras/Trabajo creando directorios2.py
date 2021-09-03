import os, io

#os.makedirs("PruebaDirectorio2")

os.chdir("PruebaDirectorio2")


archivo_enDirectorio=open("Ejemplo2.txt", "w")

archivo_enDirectorio.write("Este es un nuevo texto para el nuevo directorio")

print(os.getcwd())
print(os.listdir("./"))

archivo_enDirectorio.close()
