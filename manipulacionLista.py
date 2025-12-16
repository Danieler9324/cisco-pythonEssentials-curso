lista = [1, 2, 3, 4, 5]

reemplazo = int(input("Ingresa un numero (este sera el reemplazo del numero de en medio): "))

lista[2] = reemplazo

del lista[-1]

print(len(lista))

print(lista)

