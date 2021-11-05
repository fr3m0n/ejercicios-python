'''Write a program which takes 2 digits, X, Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i = 0, 1.., X-1
j = 0, 1, ¡Y-1.
Example
Suppose the following inputs are given to the program:
3, 5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]'''

num_filas = int(input("Ingrese numero de filas: "))
num_columnas = int(input("Ingrese numro de colunmas: "))
lista_multiple = [[0 for col in range(num_columnas)] for row in range(num_filas)]

for row in range(num_filas):
    for col in range(num_columnas):
        lista_multiple[row][col] = row*col

print(lista_multiple)
