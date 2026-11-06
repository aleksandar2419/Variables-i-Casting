# Exercici 1: àrea d'un quadrat
costat = float(input("Introdueix la mida del costat del quadrat: "))
area = costat * costat
print(f"L'àrea del quadrat és {area}")

# Exercici 2: operacions amb dos nombres enters
nombre1 = int(input("Introdueix el primer nombre enter: "))
nombre2 = int(input("Introdueix el segon nombre enter: "))

print(f"Suma: {nombre1 + nombre2}")
print(f"Resta: {nombre1 - nombre2}")
print(f"Multiplicació: {nombre1 * nombre2}")
if nombre2 != 0:
    print(f"Divisio: {nombre1 / nombre2}")
else:
    print("Divisio: no es pot dividir per zero.")

# Exercici 3: frase amb tres paraules
paraula1 = input("Introdueix la primera paraula: ")
paraula2 = input("Introdueix la segona paraula: ")
paraula3 = input("Introdueix la tercera paraula: ")
print(f"Frase: {paraula1} {paraula2} {paraula3}")

# Exercici 4: casting de dos nombres en coma flotant a enters
decimal1 = float(input("Introdueix el primer nombre en coma flotant: "))
decimal2 = float(input("Introdueix el segon nombre en coma flotant: "))
enter1 = int(decimal1)
enter2 = int(decimal2)
print(f"Els nombres enters són {enter1} i {enter2}")
