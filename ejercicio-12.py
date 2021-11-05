# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of
# a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console
# input.

valor = input("Introducir valor: ")

n1 = valor * 1
n2 = valor * 2
n3 = valor * 3
n4 = valor * 4

total = int(n1) + int(n2) + int(n3) + int(n4)
print(total)

