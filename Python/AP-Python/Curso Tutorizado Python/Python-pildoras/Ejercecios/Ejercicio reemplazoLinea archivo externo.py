from io import open

archivo_externo=open("primerArchivo.txt", "r+")

lista_archivo=archivo_externo.readlines()
lista_archivo[2]="Este texto reemplaza al anterior escribiendo desde python \n"
archivo_externo.seek(0)
archivo_externo.writelines(lista_archivo)

archivo_externo.close()
#print(lista_archivo)