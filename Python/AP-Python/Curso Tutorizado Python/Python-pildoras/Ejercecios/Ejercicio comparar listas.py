
def compararListas(lista1, lista2):

    if(len(lista1)!=len(lista2)):
        print("Las listas no son iguales")

        return False

    else:

        for i in range(0, len(lista1)):
            if(lista1[i]!=(lista2[i])):

                return False


    return True


animales1 = ["Perro", "gato", "leon", "cuervo", "zorro", "aguila"]
animales2 = ["Perro", "gato", "leon", "cuervo", "zorro", "aguila"]

print(compararListas(animales1, animales2))