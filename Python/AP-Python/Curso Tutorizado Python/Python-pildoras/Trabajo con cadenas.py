#nUsuarios=input("Introduce tu usuario: ")

#print("El usuario introducido es: " + nUsuarios.capitalize())

edad=input("Introduce tu edad por favor: ")

while(edad.isdigit()==False):

    print("El valor introducido no es correcto")

    edad=input("Introduce tu edad por favor: ")

if(int(edad)<18):

    print("No puedes pasar")

else:

    print("Puedes pasar")