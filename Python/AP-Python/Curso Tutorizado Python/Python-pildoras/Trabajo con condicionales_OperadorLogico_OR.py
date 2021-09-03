print("Obtencion beca de estudios")

nota_media=int(input("Introduce tu nota media: "))
hermanos_en_centro=int(input("Introduce nº de hermanos: "))
distancia_al_centro=int(input("Introduce distancia al centro: "))
renta_familiar=int(input("Introduce renta familiar: "))

if nota_media > 8 or hermanos_en_centro > 3 or distancia_al_centro > 10 or renta_familiar < 20000:
    print("Se te concede beca!!! ")

else:
    print("Lo sentimos. No cumples los requisitos")