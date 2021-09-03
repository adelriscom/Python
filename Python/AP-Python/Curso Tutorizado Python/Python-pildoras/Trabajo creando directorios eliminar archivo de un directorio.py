import os, io

listaArchivos=os.listdir("./")

for archivo in listaArchivos:
    
    if archivo=="Borrar.py":
        
        os.remove("Borrar.py")