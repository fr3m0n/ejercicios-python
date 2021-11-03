#Agregamos una lista vacia
lista=[]
#Recorremos el rango
for x in range(2000, 3200):
#Comprobamos si es multiplo de 7 y de 5
    if (x%7==0) and (x%5==0):
#Agregamos a la lista y lo convertimos a un string
        lista.append(str(x))
#Visualizamos por pantalla la lista
print (','.join(lista))

