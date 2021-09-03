

import random

def generarContrasegna():
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #print(mayusculas)
    minusculas = mayusculas.lower()
    #print(minusculas)
    mayusculas = list(mayusculas)
    #print(mayusculas)
    minusculas = list(minusculas)
    #print(minusculas)
    numeros = list("1234567890")
    #print(numeros)
    simbolos = list("!@#$%^&*()/-.,")
    #print(simbolos)
    
    caracterUtilizar =  mayusculas + minusculas + numeros + simbolos
    #print(caracterUtilizar)
    
    # CONTINUAR GENERAR CONTRASEÑA SEGURA
    
    contrasegna = list()
    #print(contrasegna)
    rango = random.randint(10, 20)
    
    for i in range(rango):
        caractAleat = random.choice(caracterUtilizar)
        #print(caractAleat)
        contrasegna.append(caractAleat)
        #print(contrasegna)
        
    #print(contrasegna)
    #contrasegna = "".join(contrasegna)
    contrasegna = str().join(contrasegna)
    #print(contrasegna)
    
    return contrasegna    
    
    