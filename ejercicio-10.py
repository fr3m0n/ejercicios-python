# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console
# input.

frase = input("Escriba la frase: ")
frase = list(frase)

l, d = 0, 0
for i in frase:
    if i.isalpha():
        l = l + 1
    if i.isdigit():
        d = d + 1
    else:
        pass

print("Letras:", l)
print("Digitos:", d)
