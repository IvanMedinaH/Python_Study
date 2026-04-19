"""In python blocks of code are delimited by spaces not {}
    python uses 4 spaces,
    here we have several examples of data types and its definitions
    in python
"""

#tipos de datos
#str
nombre ="Juan perez"
nombre2=""
#int
edad = 18
#float
peso = 24.50
#bool
cartilla = True
#lists
materias= ["español", "matematicas", "biologia", "quimica"]
numeros = [1, 2, 3, 4, 5]
mixta = [1, "texto", 3.14, True]
vacia = []

#diccionary (key-value pair)
datos = { "nombre":nombre,"edad":edad, "peso":peso, "cartilla":cartilla}

#tupla - lista inmutable y ordenada(el orden refiere a que mantiene posicion fija)
latLong=(1234.1234, 2345.2340)
rgb = (255,255,255)
coordenadas = (10, 20)
datos = (1, "Juan", 3.14) #mixta
unitaria = (5,)

#set (conjunto) - valores unicos sin orden y sin duplicados
deportes = {"futbol","basquetbol","natacion"}
numeros = {1, 2, 3, 4, 5}
vocales = {"a", "e", "i", "o", "u"}
vacio = set()

#valor vacio
observaciones=None
valor = None
resultado = print("hola")  

#range 
numberRange = range(0,10)
#range using a step
steppedRange= range(0,20, 2)

#bytes binary data
archivo = bytes([12,24,112,90])
#byteArray
datos = bytearray(b"Hola")
datos[0] = 72

#frozen set  - conjunto inmutable 
colores_fijos = ({"rojo","verde","negro"})
colores = frozenset({"rojo", "azul", "verde"})


#numeros complejos
numero = 3 + 4j
otro = complex(2, -3)

#typo Clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

juan = Persona("Juan", 30)
