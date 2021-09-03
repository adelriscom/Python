
cont=1
nombres=[]



while cont <= 10:

    try:

        nom = input("Ingrese el nombre " + str(cont) + ": ")
        
        if nom in nombres:
            raise ValueError
        
        else:
            nombres.append(nom)
            cont+=1
        
    except ValueError:
        
        print("Error: el nombre ya se ha introducido")
            
print("Se han registrado, " + str(cont) + " nombres")    

print(nombres)





