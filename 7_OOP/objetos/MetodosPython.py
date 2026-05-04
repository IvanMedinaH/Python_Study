"""Métodos en Clases
Un método es una función definida dentro de una clase que actúa sobre los
objetos de esa clase. Los métodos pueden acceder y modificar los atributos."""

#---------------------------------------------------
"""MÉTODO BÁSICO"""
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    # Definir un método
    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}")

# Crear un objeto y llamar el método
persona = Persona("Ana")
persona.saludar()
# Imprime: ¡Hola! Soy Ana

#---------------------------------------------------
"""MÉTODO CON PARAMETROS"""
class Calculadora:
    def __init__(self, valor_inicial=0):
        self.valor = valor_inicial

    def sumar(self, numero):
        self.valor += numero
        return self.valor

    def restar(self, numero):
        self.valor -= numero
        return self.valor

calc = Calculadora(10)
print(calc.sumar(5))
# Imprime: 15

print(calc.restar(3))
# Imprime: 12

#---------------------------------------------------
"""MÉTODO QUE RETORNA VALOR"""
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

    def calcular_perimetro(self):
        return 2 * (self.largo + self.ancho)

rectangulo = Rectangulo(5, 3)
print(f"Área: {rectangulo.calcular_area()}")
# Imprime: Área: 15

print(f"Perímetro: {rectangulo.calcular_perimetro()}")
# Imprime: Perímetro: 16

#---------------------------------------------------
"""MÉTODO QUE MODIFICA ATRIBUTOS"""
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de ${cantidad} realizado")
        else:
            print("La cantidad debe ser positiva")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de ${cantidad} realizado")
        elif cantidad > self.saldo:
            print("Saldo insuficiente")
        else:
            print("La cantidad debe ser positiva")

    def mostrar_saldo(self):
        print(f"Saldo de {self.titular}: ${self.saldo}")

cuenta = CuentaBancaria("Juan", 1000)
cuenta.depositar(500)
# Imprime: Depósito de $500 realizado

cuenta.retirar(200)
# Imprime: Retiro de $200 realizado

cuenta.mostrar_saldo()
# Imprime: Saldo de Juan: $1300

#---------------------------------------------------
"""MÉTODO __str__ Y __repr__"""
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

    def __repr__(self):
        return f"Producto('{self.nombre}', {self.precio}, {self.cantidad})"

producto = Producto("Mouse", 15, 50)
print(str(producto))
# Imprime: Mouse - $15

print(repr(producto))
# Imprime: Producto('Mouse', 15, 50)

#---------------------------------------------------
"""MÚLTIPLES MÉTODOS EN UNA CLASE"""
class Circulo:
    import math

    def __init__(self, radio):
        self.radio = radio

    def obtener_radio(self):
        return self.radio

    def calcular_area(self):
        import math
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        import math
        return 2 * math.pi * self.radio

    def aumentar_radio(self, cantidad):
        self.radio += cantidad

    def mostrar_info(self):
        import math
        print(f"Radio: {self.radio}")
        print(f"Área: {self.calcular_area():.2f}")
        print(f"Perímetro: {self.calcular_perimetro():.2f}")

circulo = Circulo(5)
circulo.mostrar_info()
# Imprime:
# Radio: 5
# Área: 78.50
# Perímetro: 31.42

circulo.aumentar_radio(3)
print(f"Nuevo radio: {circulo.obtener_radio()}")
# Imprime: Nuevo radio: 8

#---------------------------------------------------
"""MÉTODO AUXILIAR PRIVADO"""
class Contraseña:
    def __init__(self, contraseña):
        self.contraseña = contraseña

    def _es_fuerte(self):
        # Método "privado" (por convención)
        return len(self.contraseña) >= 8 and any(c.isupper() for c in self.contraseña)

    def validar(self):
        if self._es_fuerte():
            print("Contraseña fuerte ✓")
        else:
            print("Contraseña débil ✗")

pwd1 = Contraseña("123456")
pwd1.validar()
# Imprime: Contraseña débil ✗

pwd2 = Contraseña("MiContraseña123")
pwd2.validar()
# Imprime: Contraseña fuerte ✓

#---------------------------------------------------
"""MÉTODO QUE TRABAJA CON LISTAS"""
class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append({"tarea": tarea, "completada": False})

    def completar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]["completada"] = True

    def mostrar_tareas(self):
        for i, tarea in enumerate(self.tareas):
            estado = "✓" if tarea["completada"] else "✗"
            print(f"{i}: [{estado}] {tarea['tarea']}")

    def obtener_pendientes(self):
        return len([t for t in self.tareas if not t["completada"]])

lista = ListaTareas()
lista.agregar_tarea("Estudiar Python")
lista.agregar_tarea("Hacer ejercicios")
lista.agregar_tarea("Revisar conceptos")

lista.mostrar_tareas()
# Imprime:
# 0: [✗] Estudiar Python
# 1: [✗] Hacer ejercicios
# 2: [✗] Revisar conceptos

lista.completar_tarea(0)
lista.completar_tarea(1)

print(f"Tareas pendientes: {lista.obtener_pendientes()}")
# Imprime: Tareas pendientes: 1

lista.mostrar_tareas()
# Imprime:
# 0: [✓] Estudiar Python
# 1: [✓] Hacer ejercicios
# 2: [✗] Revisar conceptos
