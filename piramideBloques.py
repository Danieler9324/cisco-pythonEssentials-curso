bloques = int(input("Ingresa el numero de bloques: "))

altura = 0
capa = 1

while bloques >= capa:
    bloques -= capa
    altura += 1
    capa += 1

print("Altura:", altura)
