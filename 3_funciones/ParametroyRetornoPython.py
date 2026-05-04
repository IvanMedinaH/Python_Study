"""son datos de entrata para una funcion"""
def sumar(a, b):
    resultado = a + b
    return resultado

total = sumar(5, 3)
print(total)  # 8

"""una funcion devuelve datos con return"""
def doblar(numero):
    return numero * 2

resultado = doblar(10)
print(resultado)  # 20

"""EN PYTHON: 
Una función puede devolver varios valores como tupla."""
def obtener_coordenadas():
    return 10, 20  # Tupla

x, y = obtener_coordenadas()
print(x, y)  # 10 20

# O acceder como tupla
coords = obtener_coordenadas()
print(coords[0])  # 10


"""Parámetros que tienen un valor predeterminado si no los proporcionas."""

def saludar(nombre="Amigo"):
    print(f"¡Hola, {nombre}!")

saludar()  # ¡Hola, Amigo! (usa el valor por defecto)
saludar("Juan")  # ¡Hola, Juan! (sobrescribe el defecto)

def crear_usuario(nombre, edad=18, ciudad="Madrid"):
    print(f"{nombre}, {edad} años, {ciudad}")

crear_usuario("Ana")  # Ana, 18 años, Madrid
crear_usuario("Carlos", 25)  # Carlos, 25 años, Madrid
crear_usuario("María", 30, "Barcelona")  # María, 30 años, Barcelona
