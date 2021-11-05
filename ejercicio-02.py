# With a given integral number n, write a program to generate a dictionary that contains(i, i*i) such that is an integral number between 1 and n(both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# Consider use dict()


#Introducir un numero por pantalla (input) y que sea entero (int)
n = int(input("Escribe un numero: "))
#Creamos un diccionario vacio con la clase dict()
d = dict()
#recorremos el diccionario hasta llegar al numero introducido
for i in range(1, n+1):
#Cuando recorrenos el diccionario vamos multiplicando el numero por si mismo
    d[i] = i*i
    # d[i] = i***2
    # d.update[i] = ({i: i**2})

#Visualizamos el diccionario
print(d)
