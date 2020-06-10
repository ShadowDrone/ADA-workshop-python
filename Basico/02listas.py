# Lista de numeros
numeros = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# acumulador para ir guardando la suma
suma = 0

# itera(recorre) la lista de elementos
for n in numeros:
	suma = suma+n

# imprimo el resultado
print("La suma es ", suma)

print("**** Ahora recorro una lista de nombres")
nombres = ["Julia", "Roberto", "Susana"]

for n in nombres:
    print(n)


#imprimo con formato

print ("**** Ahora recorro con formato")
for n in nombres:
    print("Nombre {}".format(n))


#imprimo una bolsa de gatos
bolsaDeGatos = [32, "Estela", 10.3, True]

for n in bolsaDeGatos:
    print(n)
