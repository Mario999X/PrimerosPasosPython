# Escribe una función que tome una palabra y retorne con todas las letras en minúscula menos la primera y la última.


def minus(i):
    i=str(i).capitalize()
    i=str(i)[:-1] + str(i)[-1:].upper()
    i=str(i)[0]+str(i)[1:-1].lower()+str(i)[-1:]
    return i

palabra=str(input("Introduce la palabra para su consiguiente alteración: "))
print(minus(palabra))