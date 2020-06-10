#recorro con un for i, una lista de colores



colores = ["rojo", "verde", "azul", "rosa"]
i = 0

print("recorro con un while")
while i < len(colores):
    print(colores[i])
    i += 1

print("ahora recorro con un for i")

for i in range(len(colores)):
    print(colores[i])


a = 20

while a > 0:
    a = a - 1


for i in range(10):
    print("Vuelta " + str(i))