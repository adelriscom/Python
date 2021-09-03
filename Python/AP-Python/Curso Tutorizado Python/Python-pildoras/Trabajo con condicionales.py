def evaluarAlumno(nota):
    valoracion="desconocida"
    if nota < 5:
        valoracion ="suspenso"
    elif nota > 10:
        valoracion="Nota Incorrecta"
    else:
        valoracion="aprobado"
    return valoracion

    
notaAlumno=input("Introduce la nota: ")
print(evaluarAlumno(int(notaAlumno)))
