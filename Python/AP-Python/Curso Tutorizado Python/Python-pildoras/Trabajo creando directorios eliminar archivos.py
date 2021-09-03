import os, io

#os.makedirs("PruebaDirectorio2")

os.chdir("PruebaDirectorio2")


os.remove("Archivo a eliminar.txt")


print(os.getcwd())
print(os.listdir("./"))