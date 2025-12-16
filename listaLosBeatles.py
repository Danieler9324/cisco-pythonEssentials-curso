beatles = []

beatles.append("Jonh Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

for i in range (2):
    nuevo = input("Escribe un nuevo integrante: ")
    beatles.append(nuevo)

del beatles[-1]
del beatles[-1]

beatles.insert(-1, "Ringo Starr")

print("Los Fav", len(beatles))