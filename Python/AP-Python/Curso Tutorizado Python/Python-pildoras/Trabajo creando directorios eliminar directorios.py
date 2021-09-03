import io, os

os.chdir("PruebaDirectorio2")
os.remove("Ejemplo2.txt")
os.chdir("../")
os.rmdir("PruebaDirectorio2")