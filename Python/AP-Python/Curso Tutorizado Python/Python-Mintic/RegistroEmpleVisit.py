#import sys

#Programa para registrar empleados y visitantes

#Credenciales
usuario="admin"
contraseña="MisionTic2021"

#variables
usr=input("Usuario: ")
pwd=input("Contraseña: ")
menuOpcion=""
menu="""
------Menú de registro de personal-----
1. Registrar ingreso de empleado.
2. Ver empleados ingresados.
3. Registrar ingreso de visitantes.
4. Ver visitantes ingresados.
    
0. Salir
    
Ingresa un número válido de opción del menú: """

misEmpleados=""
misVisitantes=""

intentos = 1

#listas
Empleado=[]
Visitante=[]

while usr !=usuario or pwd !=contraseña:
    print("Credenciales incorrectas")
    
    #ingrese datos nuevamente
    #print("")
    usr=input("Usuario: ")
    pwd=input("Contraseña: ")
     
    intentos = intentos + 1
    
    if intentos == 4:
        break

if intentos == 4:
    print("Credenciales incorrectas")
    print("Has agotado la cantidad de intentos, por favor inicie de nuevo el programa")
    #sys.exit()
    
if usr==usuario and pwd==contraseña:
    menuOpcion=input(menu)
    while menuOpcion!=0:
                
        while menuOpcion=="1":
            emple=input("Ingresa el nombre del empleado" + " (Si no deseas agregar más, oprime la tecla SALIR): ")
            
            if emple!="SALIR":
                misEmpleados=misEmpleados + emple + ","
                #Empleado.append(emple)
            else:
                menuOpcion=input(menu)
            
        while menuOpcion=="3":
            visit=input("Ingresa el nombre del visitante" + " (Si no deseas agregar más, digite SALIR): ")
            if visit!="SALIR":
                misVisitantes+=visit + ","
                #Visitante.append(visit)
            else:
                menuOpcion=input(menu)
            
        if menuOpcion=="2":
            #print(Empleado)
            print("Los empleados registrados son: "+misEmpleados)
            menuOpcion=input(menu)
            
        elif menuOpcion=="4":
            #print(Visitante)
            print("Los visitantes registrados son: "+misVisitantes)
            menuOpcion=input(menu)
            
        elif menuOpcion=="0":
            print("¡Hasta luego!")
            
        else:
            print("Por favor ingresa una opción válida")
            menuOpcion=input(menu)
                   
    
    
       
    

