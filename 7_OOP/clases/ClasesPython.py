"""Programación Orientada a Objetos (OOP) - Clases y Objetos
Una clase es una plantilla (molde) que define la estructura y el comportamiento
de un objeto. Un objeto es una instancia de una clase."""

#---------------------------------------------------
"""CONCEPTO BASICO"""
# Definir una clase simple
class Persona:
    pass

# Crear un objeto (instancia) de la clase
persona1 = Persona()
print(type(persona1))
# Imprime: <class '__main__.Persona'>

print(isinstance(persona1, Persona))
# Imprime: True

#---------------------------------------------------
"""ATRIBUTOS DE CLASE"""
# Una clase puede tener atributos
class Auto:
    marca = "Toyota"  # Atributo de clase
    color = "Rojo"    # Atributo de clase

# Acceder a los atributos de la clase
print(Auto.marca)
# Imprime: Toyota

print(Auto.color)
# Imprime: Rojo

#---------------------------------------------------
"""ATRIBUTOS DE INSTANCIA"""
# Crear múltiples objetos y asignar atributos a cada uno
class Libro:
    pass

# Crear objetos
libro1 = Libro()
libro2 = Libro()

# Asignar atributos a cada objeto (instancia)
libro1.titulo = "Python Básico"
libro1.autor = "Juan Pérez"
libro1.paginas = 250

libro2.titulo = "Programación Avanzada"
libro2.autor = "María García"
libro2.paginas = 450

# Acceder a los atributos de cada objeto
print(f"Libro 1: {libro1.titulo} por {libro1.autor}")
# Imprime: Libro 1: Python Básico por Juan Pérez

print(f"Libro 2: {libro2.titulo} por {libro2.autor}")
# Imprime: Libro 2: Programación Avanzada por María García

#---------------------------------------------------
"""DIFERENCIA: ATRIBUTOS DE CLASE vs INSTANCIA"""
class Estudiante:
    universidad = "Universidad Nacional"  # Atributo de clase (compartido)
    contador = 0  # Atributo de clase para contar estudiantes

# Crear instancias
est1 = Estudiante()
est2 = Estudiante()

# Los atributos de clase son compartidos
print(est1.universidad)
# Imprime: Universidad Nacional

print(est2.universidad)
# Imprime: Universidad Nacional

print(Estudiante.universidad)
# Imprime: Universidad Nacional

# Pero si modificamos el atributo de instancia, no afecta la clase
est1.universidad = "Universidad Privada"
print(est1.universidad)
# Imprime: Universidad Privada

print(est2.universidad)
# Imprime: Universidad Nacional (no cambia)

print(Estudiante.universidad)
# Imprime: Universidad Nacional (no cambia)

#---------------------------------------------------
"""METODO __str__ PARA REPRESENTACION"""
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}"

producto = Producto("Laptop", 1200)
print(producto)
# Imprime: Producto: Laptop, Precio: $1200

#---------------------------------------------------
"""CREAR MULTIPLES OBJETOS"""
class Mascota:
    pass

# Crear una lista de objetos
mascotas = []

mascota1 = Mascota()
mascota1.nombre = "Max"
mascota1.tipo = "Perro"

mascota2 = Mascota()
mascota2.nombre = "Miau"
mascota2.tipo = "Gato"

mascota3 = Mascota()
mascota3.nombre = "Tweety"
mascota3.tipo = "Pájaro"

mascotas = [mascota1, mascota2, mascota3]

# Iterar sobre los objetos
for mascota in mascotas:
    print(f"{mascota.nombre} es un {mascota.tipo}")
# Imprime:
# Max es un Perro
# Miau es un Gato
# Tweety es un Pájaro

#---------------------------------------------------
"""OBJETO DENTRO DE OTRO OBJETO"""
class Direccion:
    def __init__(self, calle, ciudad):
        self.calle = calle
        self.ciudad = ciudad

class Empleado:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

# Crear un objeto Direccion
direccion = Direccion("Calle Principal 123", "Madrid")

# Crear un objeto Empleado que contiene un objeto Direccion
empleado = Empleado("Carlos", direccion)

print(f"Empleado: {empleado.nombre}")
# Imprime: Empleado: Carlos

print(f"Ciudad: {empleado.direccion.ciudad}")
# Imprime: Ciudad: Madrid
