def es_primo(numero):
    for n in range(2, numero):
        if numero % n == 0:
            return False
    print(str(numero) + " es primo")
    return True


            


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))


for i in range(num1, num2):
    es_primo(i)

        
    