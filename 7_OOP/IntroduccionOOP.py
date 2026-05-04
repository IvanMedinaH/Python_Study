"""Introducción a Programación Orientada a Objetos (OOP)
La Programación Orientada a Objetos es un paradigma que organiza el código
alrededor de "objetos" que contienen datos (atributos) y comportamientos (métodos)."""

#---------------------------------------------------
"""¿QUÉ ES UNA CLASE?"""
# Una clase es como un plano o molde para crear objetos
# Ejemplo: La clase "Coche" es el plano, un coche rojo de Toyota es un objeto

class Coche:
    # Atributos de clase (compartidos por todos los objetos)
    tipo_de_vehículo = "Automóvil"

    # Método especial que se ejecuta al crear un objeto
    def __init__(self, marca, color):
        # Atributos de instancia (únicos para cada objeto)
        self.marca = marca
        self.color = color
        self.velocidad = 0

    # Métodos (funciones dentro de la clase)
    def acelerar(self):
        self.velocidad += 10
        print(f"{self.marca} aceleró a {self.velocidad} km/h")

    def frenar(self):
        self.velocidad = 0
        print(f"{self.marca} se detuvo")

# Crear objetos (instancias) de la clase Coche
coche1 = Coche("Toyota", "Rojo")
coche2 = Coche("Honda", "Azul")

# Usar los objetos
print(f"Coche 1: {coche1.marca} - {coche1.color}")
# Imprime: Coche 1: Toyota - Rojo

print(f"Coche 2: {coche2.marca} - {coche2.color}")
# Imprime: Coche 2: Honda - Azul

coche1.acelerar()
# Imprime: Toyota aceleró a 10 km/h

coche1.acelerar()
# Imprime: Toyota aceleró a 20 km/h

coche1.frenar()
# Imprime: Toyota se detuvo

#---------------------------------------------------
"""CONCEPTOS CLAVE: ATRIBUTOS Y MÉTODOS"""
class Persona:
    # ATRIBUTOS - Datos que describe el objeto
    def __init__(self, nombre, edad, profesión):
        self.nombre = nombre      # Atributo de instancia
        self.edad = edad          # Atributo de instancia
        self.profesión = profesión  # Atributo de instancia

    # MÉTODOS - Acciones que puede realizar el objeto
    def saludar(self):
        print(f"Hola, soy {self.nombre}")

    def presentarse(self):
        print(f"Me llamo {self.nombre}, tengo {self.edad} años y soy {self.profesión}")

    def cumpleaños(self):
        self.edad += 1
        print(f"{self.nombre} ahora tiene {self.edad} años")

persona = Persona("Carlos", 25, "Ingeniero")
persona.presentarse()
# Imprime: Me llamo Carlos, tengo 25 años y soy Ingeniero

persona.cumpleaños()
# Imprime: Carlos ahora tiene 26 años

#---------------------------------------------------
"""PILARES DE LA PROGRAMACIÓN ORIENTADA A OBJETOS"""

# 1. ENCAPSULAMIENTO
# Ocultar los detalles internos y controlar el acceso
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self._titular = titular
        self._saldo = saldo_inicial  # Usar _ para indicar que es privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

    def obtener_saldo(self):
        return self._saldo

cuenta = CuentaBancaria("Juan", 1000)
print(f"Saldo: ${cuenta.obtener_saldo()}")
# Imprime: Saldo: $1000

# 2. HERENCIA
# Permitir que una clase hija herede de una clase padre
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        print("Sonido genérico")

class Gato(Animal):  # Gato hereda de Animal
    def sonido(self):
        print(f"{self.nombre}: Miau")

gato = Gato("Whiskers")
gato.sonido()
# Imprime: Whiskers: Miau

# 3. POLIMORFISMO
# Diferentes objetos pueden responder al mismo método de diferente manera
class Perro(Animal):
    def sonido(self):
        print(f"{self.nombre}: Guau")

class Pajaro(Animal):
    def sonido(self):
        print(f"{self.nombre}: Pío pío")

animales = [Gato("Miau"), Perro("Rex"), Pajaro("Tweety")]

# Todos responden a sonido() pero de diferente forma
for animal in animales:
    animal.sonido()
# Imprime:
# Miau: Miau
# Rex: Guau
# Tweety: Pío pío

#---------------------------------------------------
"""EJEMPLO COMPLETO: SISTEMA DE BIBLIOTECA"""
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        return f"{self.titulo} por {self.autor}"

class Miembro:
    def __init__(self, nombre, id_miembro):
        self.nombre = nombre
        self.id_miembro = id_miembro
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if libro.disponible:
            libro.disponible = False
            self.libros_prestados.append(libro)
            print(f"{self.nombre} pidió prestado: {libro.titulo}")
        else:
            print(f"{libro.titulo} no está disponible")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.disponible = True
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} devolvió: {libro.titulo}")

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.miembros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def registrar_miembro(self, miembro):
        self.miembros.append(miembro)

    def mostrar_libros_disponibles(self):
        print(f"Libros disponibles en {self.nombre}:")
        for libro in self.libros:
            if libro.disponible:
                print(f"  - {libro}")

# Usar el sistema
biblioteca = Biblioteca("Biblioteca Central")

# Crear y agregar libros
libro1 = Libro("Python para Principiantes", "John Smith", "123-456")
libro2 = Libro("Estructuras de Datos", "Jane Doe", "789-012")
libro3 = Libro("Algoritmos Avanzados", "Bob Johnson", "345-678")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Crear y registrar miembros
miembro1 = Miembro("Ana", "M001")
miembro2 = Miembro("Carlos", "M002")

biblioteca.registrar_miembro(miembro1)
biblioteca.registrar_miembro(miembro2)

# Mostrar libros disponibles
biblioteca.mostrar_libros_disponibles()
# Imprime:
# Libros disponibles en Biblioteca Central:
#   - Python para Principiantes por John Smith
#   - Estructuras de Datos por Jane Doe
#   - Algoritmos Avanzados por Bob Johnson

# Prestar libros
miembro1.prestar_libro(libro1)
# Imprime: Ana pidió prestado: Python para Principiantes

miembro2.prestar_libro(libro2)
# Imprime: Carlos pidió prestado: Estructuras de Datos

# Mostrar libros disponibles nuevamente
biblioteca.mostrar_libros_disponibles()
# Imprime:
# Libros disponibles en Biblioteca Central:
#   - Algoritmos Avanzados por Bob Johnson

# Devolver libro
miembro1.devolver_libro(libro1)
# Imprime: Ana devolvió: Python para Principiantes

biblioteca.mostrar_libros_disponibles()
# Imprime:
# Libros disponibles en Biblioteca Central:
#   - Python para Principiantes por John Smith
#   - Algoritmos Avanzados por Bob Johnson

#---------------------------------------------------
"""VENTAJAS DE LA PROGRAMACIÓN ORIENTADA A OBJETOS"""
print("\n" + "="*50)
print("VENTAJAS DE OOP:")
print("="*50)
print("""
1. MODULARIDAD
   - El código se organiza en módulos independientes (clases)
   - Facilita el mantenimiento y las actualizaciones

2. REUTILIZACIÓN
   - Las clases pueden reutilizarse en diferentes partes del programa
   - La herencia permite reutilizar código de clases padre

3. CLARIDAD
   - El código es más legible y fácil de entender
   - Los objetos representan entidades del mundo real

4. MANTENIBILIDAD
   - Los cambios se localizan en lugares específicos
   - Reduce el impacto de las modificaciones

5. SEGURIDAD
   - El encapsulamiento protege los datos internos
   - Se controla cómo se accede y modifica la información
""")
