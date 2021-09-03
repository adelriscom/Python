import os, io

#os.makedirs("PruebaDirectorio")

os.chdir("PruebaDirectorio")
print(os.getcwd())

archivo_enDirectorio=open("/Users/macintosh/Downloads/Curso Tutorizado Python/PruebaDirectorio/Mi archivo nuevo.txt", "w")

archivo_enDirectorio.write("Este mensaje se escribe en un archivo nuevo que debe quedar almacenado en el directorio creado")

print(os.listdir("./"))

archivo_enDirectorio.close()
