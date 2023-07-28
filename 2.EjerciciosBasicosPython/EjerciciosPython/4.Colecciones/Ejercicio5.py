# Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Crear una nueva lista 
# con los nombres ordenados alfabéticamente e imprimirla por pantalla.


listaNombres=[]
for i in range(0,5):
    listaNombres.append(str(input("Introduce el nombre de la "+ str(i+1)+ "ª persona: ")))

print(listaNombres)
nombresOrdenados= listaNombres.copy()
nombresOrdenados.sort()
print(nombresOrdenados)