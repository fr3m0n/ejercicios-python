# Write a program that computes the net amount of a bank account based a transaction log
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console
# input.

total = 0
while True:
    registro = input("Ingresar depositos y retiros: ")
    if registro == "":
        break
    else:
        registro = registro.split(" ")
        if registro[0] == "D":
            total = total + int(registro[1])
        elif registro[0] == "W":
            total = total - int(registro[1])

print(total)


