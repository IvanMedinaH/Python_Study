# Imprime números del 0 al 4
for i in range(5):
    print(i)
# Imprime:
# 0
# 1
# 2
# 3
# 4

# Con inicio y fin
for i in range(1, 6):
    print(i)
# Imprime: 1, 2, 3, 4, 5

# Con paso (step)
for i in range(0, 10, 2):
    print(i)
# Imprime: 0, 2, 4, 6, 8

# Contar hacia atrás
for i in range(5, 0, -1):
    print(i)
# Imprime: 5, 4, 3, 2, 1

"""FOR LIST, string, tuple"""
numeros = [10, 20, 30, 40, 50]

for numero in numeros:
    print(numero)
# Imprime:
# 10
# 20
# 30
# 40
# 50

# Iterar sobre strings
nombre = "Python"
for letra in nombre:
    print(letra)
# Imprime: P, y, t, h, o, n (cada una en una línea)

# Iterar sobre tuplas
tupla = (1, "Hola", 3.14)
for elemento in tupla:
    print(elemento)
# Imprime: 1, Hola, 3.14 (cada uno en una línea)

"""FOR ENUMERATE"""
frutas = ["manzana", "banana", "cereza"]

for indice, fruta in enumerate(frutas):
    print(f"Posición {indice}: {fruta}")
# Imprime:
# Posición 0: manzana
# Posición 1: banana
# Posición 2: cereza

# Con índice inicial personalizado
for indice, fruta in enumerate(frutas, 1):
    print(f"{indice}. {fruta}")
# Imprime:
# 1. manzana
# 2. banana
# 3. cereza

"""FOR ZIP"""
nombres = ["Juan", "Ana", "Carlos"]
edades = [25, 30, 28]
ciudades = ["Madrid", "Barcelona", "Valencia"]

for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")
# Imprime:
# Juan tiene 25 años y vive en Madrid
# Ana tiene 30 años y vive en Barcelona
# Carlos tiene 28 años y vive en Valencia

"""DICTIONARY"""
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Iterar sobre claves
for clave in persona:
    print(clave)
# Imprime: nombre, edad, ciudad

# Iterar sobre claves y valores
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
# Imprime:
# nombre: Juan
# edad: 30
# ciudad: Madrid

# Iterar solo sobre valores
for valor in persona.values():
    print(valor)
# Imprime: Juan, 30, Madrid