'''Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag, hello, without, world'''

frase = input("Escribe las palabras separadas por una coma: ")
palabras = [palabra for palabra in frase.split(",")]
print(", ".join(sorted(list(set(palabras)))))

