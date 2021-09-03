import queue

#Cola FIFO
#miCola=queue.Queue()

#Cola LIFO
#miCola=queue.LifoQueue()

#Cola priority
miCola=queue.PriorityQueue()

#Agregar elementos a la cola FIFO
#miCola.put("Madrid")
#miCola.put("Bogotá")
#miCola.put("México DF")

#Asignando prioridad a los elemento
miCola.put((3,"Madrid"))
miCola.put((1, "Bogotá"))
miCola.put((2, "México DF"))

#Saca el elemento
print(miCola.get())

print("A continuación se imprimen los elementos restantes de la cola")

for elemento in miCola.queue:
    
    print(elemento)
    
#Mientras que la cola no este vacia saca los elementos.
while not miCola.empty():
    
    print(miCola.get())