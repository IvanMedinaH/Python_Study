"""Herencia Simple
La herencia permite que una clase hija (subclase) herede atributos y métodos
de una clase padre (superclase). Esto facilita la reutilización de código."""

#---------------------------------------------------
"""HERENCIA BÁSICA"""
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        print(f"{self.nombre} hace un sonido")

# Crear una clase hija que hereda de Animal
class Perro(Animal):
    pass

# Crear un objeto de la clase hija
perro = Perro("Max")
print(perro.nombre)
# Imprime: Max

perro.sonido()
# Imprime: Max hace un sonido

#---------------------------------------------------
"""HERENCIA CON MÉTODO SOBRESCRITO"""
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def moverse(self):
        print(f"{self.marca} se está moviendo")

class Auto(Vehiculo):
    def moverse(self):  # Sobrescribir el método
        print(f"{self.marca} (Auto) se está moviendo por la carretera")

class Bicicleta(Vehiculo):
    def moverse(self):  # Sobrescribir el método
        print(f"{self.marca} (Bicicleta) se está moviendo pedaleando")

auto = Auto("Toyota")
auto.moverse()
# Imprime: Toyota (Auto) se está moviendo por la carretera

bicicleta = Bicicleta("Trek")
bicicleta.moverse()
# Imprime: Trek (Bicicleta) se está moviendo pedaleando

#---------------------------------------------------
"""USAR super() PARA LLAMAR AL MÉTODO DE LA CLASE PADRE"""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)  # Llamar constructor de la clase padre
        self.salario = salario

    def saludar(self):
        super().saludar()  # Llamar método de la clase padre
        print(f"Trabajo como empleado y gano ${self.salario}")

empleado = Empleado("Juan", 30, 3000)
empleado.saludar()
# Imprime:
# Hola, soy Juan
# Trabajo como empleado y gano $3000

#---------------------------------------------------
"""HERENCIA DE ATRIBUTOS Y MÉTODOS"""
class Instrumento:
    def __init__(self, nombre, material):
        self.nombre = nombre
        self.material = material

    def describir(self):
        print(f"{self.nombre} hecho de {self.material}")

class Guitarra(Instrumento):
    def __init__(self, nombre, material, cuerdas):
        super().__init__(nombre, material)
        self.cuerdas = cuerdas

    def tocar(self):
        print(f"Tocando {self.nombre} con {self.cuerdas} cuerdas")

guitarra = Guitarra("Guitarra Clásica", "Madera", 6)
guitarra.describir()
# Imprime: Guitarra Clásica hecho de Madera

guitarra.tocar()
# Imprime: Tocando Guitarra Clásica con 6 cuerdas

#---------------------------------------------------
"""MÉTODOS ADICIONALES EN LA CLASE HIJA"""
class Figuras:
    def __init__(self, color):
        self.color = color

    def obtener_color(self):
        return self.color

class Cuadrado(Figuras):
    def __init__(self, color, lado):
        super().__init__(color)
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

cuadrado = Cuadrado("rojo", 5)
print(f"Color: {cuadrado.obtener_color()}")
# Imprime: Color: rojo

print(f"Área: {cuadrado.calcular_area()}")
# Imprime: Área: 25

print(f"Perímetro: {cuadrado.calcular_perimetro()}")
# Imprime: Perímetro: 20

#---------------------------------------------------
"""VERIFICAR HERENCIA CON isinstance() y issubclass()"""
class Dispositivo:
    pass

class Teléfono(Dispositivo):
    pass

teléfono = Teléfono()

print(isinstance(teléfono, Teléfono))
# Imprime: True

print(isinstance(teléfono, Dispositivo))
# Imprime: True

print(issubclass(Teléfono, Dispositivo))
# Imprime: True

print(issubclass(Dispositivo, Teléfono))
# Imprime: False

#---------------------------------------------------
"""HERENCIA CON ATRIBUTOS PRIVADOS"""
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular
        self._saldo = saldo_inicial

    def depositar(self, cantidad):
        self._saldo += cantidad

    def obtener_saldo(self):
        return self._saldo

class CuentaAhorros(CuentaBancaria):
    def __init__(self, titular, saldo_inicial=0, interes=0.02):
        super().__init__(titular, saldo_inicial)
        self._interes = interes

    def aplicar_interes(self):
        interes_generado = self._saldo * self._interes
        self._saldo += interes_generado
        return interes_generado

cuenta = CuentaAhorros("Ana", 1000, 0.05)
print(f"Saldo inicial: ${cuenta.obtener_saldo()}")
# Imprime: Saldo inicial: $1000

interes = cuenta.aplicar_interes()
print(f"Interés generado: ${interes:.2f}")
# Imprime: Interés generado: $50.00

print(f"Saldo final: ${cuenta.obtener_saldo():.2f}")
# Imprime: Saldo final: $1050.00

#---------------------------------------------------
"""JERARQUÍA DE HERENCIA"""
class Ser:
    def respirar(self):
        print("Respirando...")

class Animal(Ser):
    def comer(self):
        print("Comiendo...")

class Mamífero(Animal):
    def amamantar(self):
        print("Amamantando...")

class Perro(Mamífero):
    def ladrar(self):
        print("¡Guau!")

perro = Perro()
perro.respirar()
# Imprime: Respirando...

perro.comer()
# Imprime: Comiendo...

perro.amamantar()
# Imprime: Amamantando...

perro.ladrar()
# Imprime: ¡Guau!

#---------------------------------------------------
"""HERENCIA Y CONSTRUCTORES"""
class Transporte:
    def __init__(self, velocidad_maxima):
        self.velocidad_maxima = velocidad_maxima

    def mostrar_velocidad(self):
        print(f"Velocidad máxima: {self.velocidad_maxima} km/h")

class Coche(Transporte):
    def __init__(self, velocidad_maxima, número_puertas):
        super().__init__(velocidad_maxima)
        self.número_puertas = número_puertas

class Bicicleta(Transporte):
    def __init__(self, velocidad_maxima, tipo):
        super().__init__(velocidad_maxima)
        self.tipo = tipo

coche = Coche(200, 4)
coche.mostrar_velocidad()
# Imprime: Velocidad máxima: 200 km/h
print(f"Puertas: {coche.número_puertas}")
# Imprime: Puertas: 4

bici = Bicicleta(40, "Montaña")
bici.mostrar_velocidad()
# Imprime: Velocidad máxima: 40 km/h
print(f"Tipo: {bici.tipo}")
# Imprime: Tipo: Montaña

#---------------------------------------------------
"""MÉTODO EN CLASE PADRE DISPONIBLE EN HIJA"""
class Forma:
    def __init__(self, color):
        self.color = color

    def describir(self):
        print(f"Soy una forma de color {self.color}")

class Triángulo(Forma):
    def __init__(self, color, base, altura):
        super().__init__(color)
        self.base = base
        self.altura = altura

    def calcular_área(self):
        return (self.base * self.altura) / 2

triangulo = Triángulo("azul", 6, 4)
triangulo.describir()  # Método heredado de Forma
# Imprime: Soy una forma de color azul

print(f"Área: {triangulo.calcular_área()}")
# Imprime: Área: 12.0
