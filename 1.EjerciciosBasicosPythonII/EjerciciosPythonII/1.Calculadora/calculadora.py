import operaciones

def main():
    """Ejemplo calculadora"""
    operando1 = int(input("Primer numero: "))
    operando2 = int(input("Segundo numero: "))
    simbolo = str(input("Simbolo: "))
    if simbolo=="+":
        resultado = operaciones.suma(operando1, operando2)
    elif simbolo=="-":
        resultado = operaciones.resta(operando1, operando2)
    elif simbolo=="x":
        resultado = operaciones.multiplica(operando1, operando2)
    elif simbolo=="/":
        resultado = operaciones.divide(operando1, operando2)
    else:
        print("Error")

    print (resultado)


main()