"""LISTS"""
numeros = [1, 2, 3, 4, 5]

# Forma simple
for numero in numeros:
    print(numero)

# Acceder por índice
for i in range(len(numeros)):
    print(f"Posición {i}: {numeros[i]}")
# Imprime:
# Posición 0: 1
# Posición 1: 2
# Posición 2: 3
# Posición 3: 4
# Posición 4: 5

# List comprehension (crear lista modificada)
cuadrados = [x**2 for x in numeros]
print(cuadrados)
# Imprime: [1, 4, 9, 16, 25]

# Filtrar elementos
pares = [x for x in numeros if x % 2 == 0]
print(pares)
# Imprime: [2, 4]

"""TUPLES"""
coordenadas = (10, 20, 30)

for valor in coordenadas:
    print(valor)
# Imprime: 10, 20, 30

# Desempaquetado
tupla = (1, 2, 3)
a, b, c = tupla
print(a, b, c)
# Imprime: 1 2 3

# Iterar sobre tupla de tuplas
puntos = [(10, 20), (30, 40), (50, 60)]
for x, y in puntos:
    print(f"x={x}, y={y}")
# Imprime:
# x=10, y=20
# x=30, y=40
# x=50, y=60

"""DICTIONARY"""
estudiante = {"nombre": "Juan", "edad": 20, "materia": "Python"}

# Por claves
for clave in estudiante:
    print(clave)
# Imprime: nombre, edad, materia

# Por claves y valores
for clave, valor in estudiante.items():
    print(f"{clave} = {valor}")
# Imprime:
# nombre = Juan
# edad = 20
# materia = Python

# Por valores
for valor in estudiante.values():
    print(valor)
# Imprime: Juan, 20, Python

# Diccionario con listas
calificaciones = {
    "Juan": [85, 90, 88],
    "Ana": [92, 89, 94],
    "Carlos": [78, 82, 80]
}

for nombre, notas in calificaciones.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: promedio = {promedio:.2f}")
# Imprime:
# Juan: promedio = 87.67
# Ana: promedio = 91.67
# Carlos: promedio = 80.00


"""STRING"""
texto = "Python"

for letra in texto:
    print(letra)
# Imprime: P, y, t, h, o, n (cada una en una línea)

# Iterar con índice
for indice, letra in enumerate(texto):
    print(f"{indice}: {letra}")
# Imprime:
# 0: P
# 1: y
# 2: t
# 3: h
# 4: o
# 5: n

"""SET"""
numeros = {1, 2, 3, 4, 5}

for numero in numeros:
    print(numero)
# Imprime: 1, 2, 3, 4, 5 (en orden indefinido, los sets no tienen orden)

# Set comprehension (crear set modificado)
cuadrados = {x**2 for x in numeros}
print(cuadrados)
# Imprime: {1, 4, 9, 16, 25}