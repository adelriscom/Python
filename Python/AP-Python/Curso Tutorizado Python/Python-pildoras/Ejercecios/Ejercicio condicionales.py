print("Ejercicio Tipo impositivo delaracion de renta")

renta = float(input("Introduce la renta: "))

if renta < 12000:
    print("A la renta " + str(renta) + " le coresponde  7% de tipo impositivo")

elif renta > 12000 and renta < 18000:                                    
    print("A la renta " + str(renta) + " le coresponde  15% de tipo impositivo")

elif renta > 18000 and renta < 35000:
    print("A la renta " + str(renta) + " le coresponde  21% de tipo impositivo")

elif renta > 35000 and renta < 70000:
    print("A la renta " + str(renta) + " le coresponde  35% de tipo impositivo")

else:
    print("A la renta " + str(renta) + " le coresponde  45% de tipo impositivo")


