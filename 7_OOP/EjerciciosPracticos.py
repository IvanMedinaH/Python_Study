"""Ejercicios Prácticos de Programación Orientada a Objetos
Estos ejercicios refuerzan los conceptos aprendidos sobre clases, métodos,
constructores, encapsulamiento y herencia."""

#---------------------------------------------------
"""EJERCICIO 1: CLASE ESTUDIANTE"""
# Crear una clase Estudiante con atributos: nombre, edad, calificaciones (lista)
# Métodos: agregar_calificacion(), calcular_promedio(), mostrar_info()

class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        if 0 <= calificacion <= 100:
            self.calificaciones.append(calificacion)
        else:
            print("La calificación debe estar entre 0 y 100")

    def calcular_promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

    def mostrar_info(self):
        promedio = self.calcular_promedio()
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Promedio: {promedio:.2f}")

# Usar la clase
est = Estudiante("María", 20)
est.agregar_calificacion(85)
est.agregar_calificacion(90)
est.agregar_calificacion(78)
est.mostrar_info()
# Imprime:
# Nombre: María
# Edad: 20
# Promedio: 84.33

#---------------------------------------------------
"""EJERCICIO 2: CLASE RECTANGULO CON VALIDACIÓN"""
# Crear una clase Rectángulo con validación en el constructor
# Atributos: largo, ancho
# Métodos: area(), perimetro(), cambiar_dimensiones()

class Rectangulo:
    def __init__(self, largo, ancho):
        if largo > 0 and ancho > 0:
            self.largo = largo
            self.ancho = ancho
        else:
            print("Error: Las dimensiones deben ser positivas")
            self.largo = 1
            self.ancho = 1

    def area(self):
        return self.largo * self.ancho

    def perimetro(self):
        return 2 * (self.largo + self.ancho)

    def cambiar_dimensiones(self, nuevo_largo, nuevo_ancho):
        if nuevo_largo > 0 and nuevo_ancho > 0:
            self.largo = nuevo_largo
            self.ancho = nuevo_ancho
        else:
            print("Error: Las dimensiones deben ser positivas")

# Usar la clase
rect = Rectangulo(5, 3)
print(f"Área: {rect.area()}")
# Imprime: Área: 15

print(f"Perímetro: {rect.perimetro()}")
# Imprime: Perímetro: 16

rect.cambiar_dimensiones(8, 6)
print(f"Nueva área: {rect.area()}")
# Imprime: Nueva área: 48

#---------------------------------------------------
"""EJERCICIO 3: CLASE CON ENCAPSULAMIENTO"""
# Crear una clase Temperatura que convierta entre Celsius, Fahrenheit y Kelvin
# Usar encapsulamiento para proteger los atributos

class Temperatura:
    def __init__(self, celsius):
        self._celsius = celsius

    def get_celsius(self):
        return self._celsius

    def set_celsius(self, celsius):
        if celsius > -273.15:
            self._celsius = celsius
        else:
            print("Error: Temperatura bajo cero absoluto")

    def get_fahrenheit(self):
        return (self._celsius * 9/5) + 32

    def get_kelvin(self):
        return self._celsius + 273.15

    def __str__(self):
        return f"{self._celsius}°C = {self.get_fahrenheit():.2f}°F = {self.get_kelvin():.2f}K"

# Usar la clase
temp = Temperatura(25)
print(temp)
# Imprime: 25°C = 77.00°F = 298.15K

temp.set_celsius(0)
print(temp)
# Imprime: 0°C = 32.00°F = 273.15K

#---------------------------------------------------
"""EJERCICIO 4: HERENCIA SIMPLE"""
# Crear una clase Vehiculo y dos clases que hereden de ella: Auto y Motocicleta
# Cada una debe tener métodos específicos

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        print(f"{self.marca} {self.modelo}")

class Auto(Vehiculo):
    def __init__(self, marca, modelo, número_puertas):
        super().__init__(marca, modelo)
        self.número_puertas = número_puertas

    def describir(self):
        super().describir()
        print(f"Puertas: {self.número_puertas}")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo_manillar):
        super().__init__(marca, modelo)
        self.tipo_manillar = tipo_manillar

    def describir(self):
        super().describir()
        print(f"Tipo de manillar: {self.tipo_manillar}")

# Usar las clases
auto = Auto("Toyota", "Corolla", 4)
auto.describir()
# Imprime:
# Toyota Corolla
# Puertas: 4

moto = Motocicleta("Harley Davidson", "Street 750", "Tipo Cruiser")
moto.describir()
# Imprime:
# Harley Davidson Street 750
# Tipo de manillar: Tipo Cruiser

#---------------------------------------------------
"""EJERCICIO 5: LISTA DE OBJETOS"""
# Crear una clase Carrito de compras que contenga una lista de Productos
# Métodos: agregar_producto(), eliminar_producto(), calcular_total()

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def obtener_subtotal(self):
        return self.precio * self.cantidad

class CarritoCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, nombre):
        self.productos = [p for p in self.productos if p.nombre != nombre]

    def calcular_total(self):
        return sum(p.obtener_subtotal() for p in self.productos)

    def mostrar_carrito(self):
        print("=== Carrito de Compras ===")
        for producto in self.productos:
            print(f"{producto.nombre}: ${producto.precio} x {producto.cantidad} = ${producto.obtener_subtotal()}")
        print(f"Total: ${self.calcular_total()}")

# Usar las clases
carrito = CarritoCompras()
carrito.agregar_producto(Producto("Laptop", 1000, 1))
carrito.agregar_producto(Producto("Mouse", 25, 2))
carrito.agregar_producto(Producto("Teclado", 80, 1))

carrito.mostrar_carrito()
# Imprime:
# === Carrito de Compras ===
# Laptop: $1000 x 1 = $1000
# Mouse: $25 x 2 = $50
# Teclado: $80 x 1 = $80
# Total: $1130

carrito.eliminar_producto("Mouse")
print()
carrito.mostrar_carrito()
# Imprime:
# === Carrito de Compras ===
# Laptop: $1000 x 1 = $1000
# Teclado: $80 x 1 = $80
# Total: $1080

#---------------------------------------------------
"""EJERCICIO 6: POLIMORFISMO"""
# Crear diferentes animales que respondan al método sonido() de forma diferente

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        return f"{self.nombre}: ¡Guau guau!"

class Gato(Animal):
    def sonido(self):
        return f"{self.nombre}: Miau miau"

class Vaca(Animal):
    def sonido(self):
        return f"{self.nombre}: Muuu"

class Pajaro(Animal):
    def sonido(self):
        return f"{self.nombre}: Pío pío"

# Usar polimorfismo
animales = [
    Perro("Rex"),
    Gato("Misu"),
    Vaca("Bessie"),
    Pajaro("Tweety")
]

print("=== Sonidos de Animales ===")
for animal in animales:
    print(animal.sonido())
# Imprime:
# === Sonidos de Animales ===
# Rex: ¡Guau guau!
# Misu: Miau miau
# Bessie: Muuu
# Tweety: Pío pío

#---------------------------------------------------
"""EJERCICIO 7: CLASE CON MÉTODOS PRIVADOS"""
# Crear una clase Contraseña que valide y encripte contraseñas

class Contraseña:
    def __init__(self, contraseña):
        if self._es_valida(contraseña):
            self._contraseña = self._encriptar(contraseña)
        else:
            print("Contraseña no válida")
            self._contraseña = None

    def _es_valida(self, contraseña):
        return len(contraseña) >= 8

    def _encriptar(self, contraseña):
        return contraseña[::-1]  # Invertir la cadena

    def verificar(self, intento):
        return self._encriptar(intento) == self._contraseña

# Usar la clase
pwd = Contraseña("MiSeguraContraseña123")
print(f"Verificar correcta: {pwd.verificar('MiSeguraContraseña123')}")
# Imprime: Verificar correcta: True

print(f"Verificar incorrecta: {pwd.verificar('OtraContraseña')}")
# Imprime: Verificar incorrecta: False

#---------------------------------------------------
"""EJERCICIO 8: JERARQUÍA DE HERENCIA"""
# Crear una jerarquía: Persona -> Empleado -> Gerente

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Empleado(Persona):
    def __init__(self, nombre, id_empleado, salario):
        super().__init__(nombre)
        self.id_empleado = id_empleado
        self.salario = salario

    def info(self):
        print(f"Empleado: {self.nombre} (ID: {self.id_empleado}, Salario: ${self.salario})")

class Gerente(Empleado):
    def __init__(self, nombre, id_empleado, salario, departamento):
        super().__init__(nombre, id_empleado, salario)
        self.departamento = departamento

    def info(self):
        super().info()
        print(f"Departamento: {self.departamento}")

# Usar las clases
emp = Empleado("Juan", "E001", 2500)
emp.info()
# Imprime: Empleado: Juan (ID: E001, Salario: $2500)

gerente = Gerente("Ana", "G001", 4500, "Tecnología")
gerente.info()
# Imprime:
# Empleado: Ana (ID: G001, Salario: $4500)
# Departamento: Tecnología

print("\n✓ ¡Todos los ejercicios completados!")
