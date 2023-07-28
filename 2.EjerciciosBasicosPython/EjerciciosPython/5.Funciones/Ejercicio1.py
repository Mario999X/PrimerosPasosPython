# Confeccionar un programa que calcule el factorial de un número introducido por teclado.


def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1

num= int(input("Introduzca un número para saber su factorial a continuación: "))
print(factorial(num))