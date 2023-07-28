import empleado as emp

lista = []

def main():
    salir = False
    while salir == False:
        teclado = int(input("""
        0 para salir
        1 para introducir empleados
        2 para despedirlos: """))

        if teclado == 0:
            salir = True

        elif teclado == 1:
            empleado = emp.empleado()
            empleado.nombre = str(input("Nombre: "))
            empleado.id = int(input("ID: "))
            lista.append(empleado)
            for i in lista:
                print("Nombre: "+i.nombre+" |ID: " + str(i.id))


        elif teclado == 2:
            despedir = int(input("ID: "))
            for i in lista:
                if(i.id == despedir):
                    lista.remove(i)
                else:
                    print("ID incorrecto")
        
        else:
            print("Error")

main()
