"""Encapsulamiento Básico
El encapsulamiento es el principio de ocultar los detalles internos de una clase
y proporcionar una interfaz pública controlada. En Python, se usa la convención
de un guion bajo (_) para indicar que un atributo o método es "privado"."""

#---------------------------------------------------
"""ATRIBUTOS PÚBLICOS vs PRIVADOS (CONVENCIÓN)"""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público
        self._edad = edad     # Atributo "privado" (por convención)

persona = Persona("Juan", 30)

# Se puede acceder a atributos públicos directamente
print(f"Nombre: {persona.nombre}")
# Imprime: Nombre: Juan

# Técnicamente se puede acceder a _edad, pero NO DEBE hacerse
# (es solo una convención, no una restricción real)
print(f"Edad (no recomendado): {persona._edad}")
# Imprime: Edad (no recomendado): 30

#---------------------------------------------------
"""MÉTODOS PÚBLICOS vs PRIVADOS"""
class CuentaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo  # Atributo privado

    def depositar(self, cantidad):  # Método público
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Depósito exitoso. Saldo: ${self._saldo}")

    def retirar(self, cantidad):  # Método público
        if self._validar_saldo(cantidad):  # Llamar método privado
            self._saldo -= cantidad
            print(f"Retiro exitoso. Saldo: ${self._saldo}")
        else:
            print("Saldo insuficiente")

    def _validar_saldo(self, cantidad):  # Método privado (por convención)
        return cantidad > 0 and cantidad <= self._saldo

cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
# Imprime: Depósito exitoso. Saldo: $1500

cuenta.retirar(200)
# Imprime: Retiro exitoso. Saldo: $1300

# NO se debe llamar directamente a métodos privados
# cuenta._validar_saldo(100)  # Evitar esto

#---------------------------------------------------
"""GETTERS (MÉTODOS PARA OBTENER VALORES)"""
class Temperatura:
    def __init__(self, celsius):
        self._celsius = celsius

    def get_celsius(self):
        return self._celsius

    def get_fahrenheit(self):
        return (self._celsius * 9/5) + 32

    def get_kelvin(self):
        return self._celsius + 273.15

temp = Temperatura(25)
print(f"Celsius: {temp.get_celsius()}°C")
# Imprime: Celsius: 25°C

print(f"Fahrenheit: {temp.get_fahrenheit()}°F")
# Imprime: Fahrenheit: 77.0°F

print(f"Kelvin: {temp.get_kelvin()}K")
# Imprime: Kelvin: 298.15K

#---------------------------------------------------
"""SETTERS (MÉTODOS PARA ESTABLECER VALORES)"""
class Estudiante:
    def __init__(self, nombre):
        self._nombre = nombre
        self._calificacion = 0

    def set_calificacion(self, calificacion):
        if 0 <= calificacion <= 100:
            self._calificacion = calificacion
        else:
            print("Error: La calificación debe estar entre 0 y 100")

    def get_calificacion(self):
        return self._calificacion

est = Estudiante("Ana")
est.set_calificacion(85)
print(f"Calificación: {est.get_calificacion()}")
# Imprime: Calificación: 85

est.set_calificacion(150)
# Imprime: Error: La calificación debe estar entre 0 y 100

#---------------------------------------------------
"""ENCAPSULAMIENTO CON VALIDACIÓN"""
class Usuario:
    def __init__(self, nombre, contraseña):
        self._nombre = nombre
        self._contraseña = self._encriptar(contraseña)

    def _encriptar(self, contraseña):
        # Método privado para encriptar (ejemplo simple)
        return contraseña[::-1]  # Solo invertimos la cadena

    def verificar_contraseña(self, contraseña):
        return self._encriptar(contraseña) == self._contraseña

    def cambiar_contraseña(self, contraseña_antigua, contraseña_nueva):
        if self.verificar_contraseña(contraseña_antigua):
            self._contraseña = self._encriptar(contraseña_nueva)
            print("Contraseña cambida exitosamente")
        else:
            print("Contraseña antigua incorrecta")

usuario = Usuario("Juan", "MiContraseña")
print(f"Verificar contraseña correcta: {usuario.verificar_contraseña('MiContraseña')}")
# Imprime: Verificar contraseña correcta: True

print(f"Verificar contraseña incorrecta: {usuario.verificar_contraseña('OtraContraseña')}")
# Imprime: Verificar contraseña incorrecta: False

usuario.cambiar_contraseña("MiContraseña", "NuevaContraseña")
# Imprime: Contraseña cambida exitosamente

#---------------------------------------------------
"""PROPIEDADES (@property)"""
class Circulo:
    def __init__(self, radio):
        self._radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, valor):
        if valor > 0:
            self._radio = valor
        else:
            print("El radio debe ser positivo")

    @property
    def area(self):
        import math
        return math.pi * self._radio ** 2

circulo = Circulo(5)
print(f"Radio: {circulo.radio}")
# Imprime: Radio: 5

print(f"Área: {circulo.area:.2f}")
# Imprime: Área: 78.50

circulo.radio = 10
print(f"Nuevo área: {circulo.area:.2f}")
# Imprime: Nuevo área: 314.16

circulo.radio = -5
# Imprime: El radio debe ser positivo

#---------------------------------------------------
"""ENCAPSULAMIENTO EN LISTA"""
class ListaSegura:
    def __init__(self):
        self._items = []

    def agregar(self, item):
        if item not in self._items:
            self._items.append(item)
        else:
            print(f"{item} ya existe en la lista")

    def eliminar(self, item):
        if item in self._items:
            self._items.remove(item)
        else:
            print(f"{item} no existe en la lista")

    def obtener_todos(self):
        return self._items.copy()  # Retornar copia, no el original

    def obtener_cantidad(self):
        return len(self._items)

lista = ListaSegura()
lista.agregar("Python")
lista.agregar("Java")
lista.agregar("Python")
# Imprime: Python ya existe en la lista

print(f"Items: {lista.obtener_todos()}")
# Imprime: Items: ['Python', 'Java']

print(f"Cantidad: {lista.obtener_cantidad()}")
# Imprime: Cantidad: 2

#---------------------------------------------------
"""MÉTODOS PRIVADOS PARA LÓGICA INTERNA"""
class Producto:
    def __init__(self, nombre, precio, impuesto=0.21):
        self._nombre = nombre
        self._precio = precio
        self._impuesto = impuesto

    def _calcular_impuesto(self):
        return self._precio * self._impuesto

    def _calcular_total(self):
        return self._precio + self._calcular_impuesto()

    def mostrar_info(self):
        print(f"Producto: {self._nombre}")
        print(f"Precio: ${self._precio:.2f}")
        print(f"Impuesto: ${self._calcular_impuesto():.2f}")
        print(f"Total: ${self._calcular_total():.2f}")

producto = Producto("Laptop", 1000)
producto.mostrar_info()
# Imprime:
# Producto: Laptop
# Precio: $1000.00
# Impuesto: $210.00
# Total: $1210.00

#---------------------------------------------------
"""DOUBLE UNDERSCORE (NAME MANGLING)"""
class Secreto:
    def __init__(self, secreto):
        self.__secreto = secreto  # Double underscore

    def mostrar(self):
        return self.__secreto

obj = Secreto("Mi secreto")
print(obj.mostrar())
# Imprime: Mi secreto

# Python hace "name mangling" con double underscore
# No se puede acceder directamente: print(obj.__secreto)  # Error
# Pero existe como: print(obj._Secreto__secreto)  # Técnicamente sí, pero NO HACER
