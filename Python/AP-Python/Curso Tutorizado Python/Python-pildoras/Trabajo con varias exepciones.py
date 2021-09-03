def divide():

    try:

        op1=float(input("Introduce el primer numero: "))
        op2=float(input("Introduce el segundo numero: "))

        print("El resulta es: " + str(op1/op2))
    
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    except ValueError:
        print("El valor introducido no es numérico")

divide()
print("Calculo finalizado. Continuamos con el programa")