# Write a program that accepts a sentence and calculate the number of upper case letters and
# lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console
# input.

frase = input("Entrar la frase: ")
frase = list(frase)

u, l = 0, 0
for i in frase:
    if i.isupper():
        u = u + 1
    if i.islower():
        l = l + 1
    else:
        pass

print("Mayuscula:", u)
print("Minuscula:", l)

