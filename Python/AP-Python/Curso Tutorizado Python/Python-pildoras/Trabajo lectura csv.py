import csv

with open('posts.csv', 'r', newline='') as csvfile:
    postreader = csv.reader(csvfile, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    for fila in postreader:
        print(','.join(fila))
        print()