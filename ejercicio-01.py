# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# Hints:
# Consider use range(  # begin, #end) method

#Agregamos una lista vacia
lista=[]
#Recorremos el rango
for x in range(2000, 3200):
#Comprobamos si es multiplo de 7 y de 5
    if (x%7==0) and (x%5==0):
#Agregamos a la lista y lo convertimos a un string
        lista.append(str(x))
#Visualizamos por pantalla la lista separadas por comas
print (','.join(lista))

