"""Constructores (__init__)
El constructor (__init__) es un método especial que se ejecuta automáticamente
cuando se crea un objeto. Se usa para inicializar los atributos de la clase."""

#---------------------------------------------------
"""CONSTRUCTOR BÁSICO"""
class Persona:
    def __init__(self, nombre):
        print(f"Se creó una persona con el nombre: {nombre}")
        self.nombre = nombre

# El constructor se ejecuta automáticamente al crear el objeto
persona = Persona("Carlos")
# Imprime: Se creó una persona con el nombre: Carlos

print(persona.nombre)
# Imprime: Carlos

#---------------------------------------------------
"""CONSTRUCTOR CON MÚLTIPLES PARÁMETROS"""
class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

# Crear autos con diferentes valores
auto1 = Auto("Toyota", "Corolla", 2022)
print(f"{auto1.marca} {auto1.modelo} - Año: {auto1.año}")
# Imprime: Toyota Corolla - Año: 2022

auto2 = Auto("Honda", "Civic", 2023)
print(f"{auto2.marca} {auto2.modelo} - Año: {auto2.año}")
# Imprime: Honda Civic - Año: 2023

#---------------------------------------------------
"""PARÁMETROS CON VALORES POR DEFECTO"""
class Videojuego:
    def __init__(self, titulo, genero, año=2024):
        self.titulo = titulo
        self.genero = genero
        self.año = año

# Con parámetro por defecto
juego1 = Videojuego("Elden Ring", "Action RPG")
print(f"{juego1.titulo} ({juego1.año})")
# Imprime: Elden Ring (2024)

# Sin parámetro por defecto
juego2 = Videojuego("The Legend of Zelda", "Action-Adventure", 2017)
print(f"{juego2.titulo} ({juego2.año})")
# Imprime: The Legend of Zelda (2017)

#---------------------------------------------------
"""INICIALIZACIÓN DE MÚLTIPLES ATRIBUTOS"""
class CuentaBancaria:
    def __init__(self, titular, tipo_cuenta="Ahorros", saldo=0, interes=0.02):
        self.titular = titular
        self.tipo_cuenta = tipo_cuenta
        self.saldo = saldo
        self.interes = interes

cuenta1 = CuentaBancaria("Juan", "Corriente", 5000)
print(f"Titular: {cuenta1.titular}")
print(f"Tipo: {cuenta1.tipo_cuenta}")
print(f"Saldo: ${cuenta1.saldo}")
print(f"Interés: {cuenta1.interes * 100}%")
# Imprime:
# Titular: Juan
# Tipo: Corriente
# Saldo: $5000
# Interés: 2.0%

#---------------------------------------------------
"""CONSTRUCTOR QUE CALCULA VALORES"""
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
        self.area = largo * ancho  # Calcular en el constructor
        self.perimetro = 2 * (largo + ancho)

rect = Rectangulo(5, 3)
print(f"Dimensiones: {rect.largo} x {rect.ancho}")
print(f"Área: {rect.area}")
print(f"Perímetro: {rect.perimetro}")
# Imprime:
# Dimensiones: 5 x 3
# Área: 15
# Perímetro: 16

#---------------------------------------------------
"""CONSTRUCTOR CON VALIDACIÓN"""
class Edad:
    def __init__(self, edad):
        if edad < 0:
            print("Error: La edad no puede ser negativa")
            self.edad = 0
        elif edad > 120:
            print("Error: La edad es demasiado alta")
            self.edad = 120
        else:
            self.edad = edad

persona1 = Edad(25)
print(f"Edad: {persona1.edad}")
# Imprime: Edad: 25

persona2 = Edad(-5)
# Imprime: Error: La edad no puede ser negativa
print(f"Edad: {persona2.edad}")
# Imprime: Edad: 0

persona3 = Edad(150)
# Imprime: Error: La edad es demasiado alta
print(f"Edad: {persona3.edad}")
# Imprime: Edad: 120

#---------------------------------------------------
"""CONSTRUCTOR CON LISTA"""
class Estudiante:
    def __init__(self, nombre, materias=None):
        self.nombre = nombre
        self.materias = materias if materias is not None else []

est1 = Estudiante("Ana")
print(f"{est1.nombre} - Materias: {est1.materias}")
# Imprime: Ana - Materias: []

est2 = Estudiante("Pedro", ["Matemáticas", "Física", "Química"])
print(f"{est2.nombre} - Materias: {est2.materias}")
# Imprime: Pedro - Materias: ['Matemáticas', 'Física', 'Química']

#---------------------------------------------------
"""CONSTRUCTOR QUE CREA OBJETOS INTERNOS"""
class Dirección:
    def __init__(self, calle, ciudad, código_postal):
        self.calle = calle
        self.ciudad = ciudad
        self.código_postal = código_postal

class Empresa:
    def __init__(self, nombre, calle, ciudad, código_postal):
        self.nombre = nombre
        # Crear un objeto Dirección dentro del constructor
        self.dirección = Dirección(calle, ciudad, código_postal)

empresa = Empresa("TechCorp", "Calle Principal 123", "Madrid", "28001")
print(f"Empresa: {empresa.nombre}")
print(f"Ubicación: {empresa.dirección.calle}, {empresa.dirección.ciudad}")
# Imprime:
# Empresa: TechCorp
# Ubicación: Calle Principal 123, Madrid

#---------------------------------------------------
"""CONSTRUCTOR SIN PARÁMETROS (EXCEPTO SELF)"""
class Reloj:
    def __init__(self):
        self.hora = "00:00:00"
        self.zona_horaria = "UTC"

reloj = Reloj()
print(f"Hora: {reloj.hora}")
print(f"Zona horaria: {reloj.zona_horaria}")
# Imprime:
# Hora: 00:00:00
# Zona horaria: UTC

#---------------------------------------------------
"""CONTADOR DE OBJETOS CREADOS"""
class Usuario:
    cantidad_usuarios = 0  # Variable de clase

    def __init__(self, nombre):
        self.nombre = nombre
        Usuario.cantidad_usuarios += 1  # Incrementar cada vez que se crea un usuario

usuario1 = Usuario("Alice")
print(f"Usuarios creados: {Usuario.cantidad_usuarios}")
# Imprime: Usuarios creados: 1

usuario2 = Usuario("Bob")
print(f"Usuarios creados: {Usuario.cantidad_usuarios}")
# Imprime: Usuarios creados: 2

usuario3 = Usuario("Charlie")
print(f"Usuarios creados: {Usuario.cantidad_usuarios}")
# Imprime: Usuarios creados: 3

#---------------------------------------------------
"""CONSTRUCTOR CON PROCESAMIENTO DE DATOS"""
class Email:
    def __init__(self, correo):
        # Procesar el correo durante la inicialización
        if "@" in correo and "." in correo:
            self.correo = correo.lower()
            self.usuario = correo.split("@")[0]
            self.dominio = correo.split("@")[1]
        else:
            print("Correo inválido")
            self.correo = None

email = Email("Juan.Perez@Gmail.com")
print(f"Correo: {email.correo}")
print(f"Usuario: {email.usuario}")
print(f"Dominio: {email.dominio}")
# Imprime:
# Correo: juan.perez@gmail.com
# Usuario: juan.perez
# Dominio: Gmail.com
