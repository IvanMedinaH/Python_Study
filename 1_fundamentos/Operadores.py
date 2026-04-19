"""Operators in python define which types of data can be used with, 
and what operations are allowed with them"""

"""ARITHMETIC"""

a = 10
b = 3

print(a + b)      # 13 - SUMA
print(a - b)      # 7  - RESTA
print(a * b)      # 30 - MULTIPLICACIÓN
print(a / b)      # 3.333... - DIVISIÓN (resultado float)
print(a // b)     # 3  - DIVISIÓN ENTERA (sin decimales)
print(a % b)      # 1  - MÓDULO (residuo de la división)
print(a ** b)     # 1000 - POTENCIA (elevado a)
print(-a)         # -10 - NEGACIÓN (cambiar signo)
print(+a)         # 10 - AFIRMACIÓN (mantener signo)

"""ASSIGNMENT"""
x = 10           # Asignación simple
x += 5           # x = x + 5 (suma y asigna)
x -= 3           # x = x - 3 (resta y asigna)
x *= 2           # x = x * 2 (multiplica y asigna)
x /= 4           # x = x / 4 (divide y asigna)
x //= 2          # x = x // 2 (división entera y asigna)
x %= 3           # x = x % 3 (módulo y asigna)
x **= 2          # x = x ** 2 (potencia y asigna)
x &= 5           # x = x & 5 (AND binario y asigna)
x |= 5           # x = x | 5 (OR binario y asigna)
x ^= 5           # x = x ^ 5 (XOR binario y asigna)
x >>= 2          # x = x >> 2 (desplaza a la derecha y asigna)
x <<= 2          # x = x << 2 (desplaza a la izquierda y asigna)

"""COMPARISON"""
a = 10
b = 5

print(a == b)    # False - IGUAL A
print(a != b)    # True  - NO IGUAL A
print(a > b)     # True  - MAYOR QUE
print(a < b)     # False - MENOR QUE
print(a >= b)    # True  - MAYOR O IGUAL QUE
print(a <= b)    # False - MENOR O IGUAL QUE

"""LOGIC OPERATOR""" 
a = True
b = False

print(a and b)      # False - AND lógico (ambos deben ser True)
print(a or b)       # True  - OR lógico (al menos uno debe ser True)
print(not a)        # False - NOT lógico (invierte el valor)

edad = 25
print(edad > 18 and edad < 65)  # True - está en el rango
print(edad < 18 or edad > 65)   # False - no es jubilado ni menor

"""IDENTITY"""
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is c)       # True  - SON EL MISMO OBJETO
print(a is b)       # False - SON OBJETOS DIFERENTES (aunque tienen igual contenido)
print(a is not b)   # True  - NO SON EL MISMO OBJETO
print(a == b)       # True  - TIENEN EL MISMO CONTENIDO

"""MEMBERSHIP op"""
lista = [1, 2, 3, 4, 5]
texto = "Hola"

print(3 in lista)        # True  - 3 ESTÁ EN LA LISTA
print(10 in lista)       # False - 10 NO ESTÁ EN LA LISTA
print(10 not in lista)   # True  - 10 NO ESTÁ EN LA LISTA
print("H" in texto)      # True  - "H" ESTÁ EN EL TEXTO
print("x" not in texto)  # True  - "x" NO ESTÁ EN EL TEXTO

"""BIT TO BIT"""
a = 5      # 0101 en binario
b = 3      # 0011 en binario

print(a & b)    # 1     - AND BINARIO (0101 & 0011 = 0001)
print(a | b)    # 7     - OR BINARIO (0101 | 0011 = 0111)
print(a ^ b)    # 6     - XOR BINARIO (0101 ^ 0011 = 0110)
print(~a)       # -6    - NOT BINARIO (invierte todos los bits)
print(a << 2)   # 20    - DESPLAZAMIENTO A IZQUIERDA (0101 << 2 = 10100)
print(a >> 1)   # 2     - DESPLAZAMIENTO A DERECHA (0101 >> 1 = 0010)

"""STRING op"""
str1 = "Hola"
str2 = "Mundo"

print(str1 + str2)      # HolaMundo - CONCATENACIÓN
print(str1 + " " + str2) # Hola Mundo

print("Ha" * 3)         # HaHaHa - REPETICIÓN
print(str1[0])          # H - INDEXACIÓN (acceso por posición)
print(str1[0:3])        # Hol - SLICING (rango de caracteres)

"""LIST """
lista1 = [1, 2, 3]
lista2 = [4, 5]

print(lista1 + lista2)  # [1, 2, 3, 4, 5] - CONCATENACIÓN
print(lista1 * 2)       # [1, 2, 3, 1, 2, 3] - REPETICIÓN
print(lista1[0])        # 1 - INDEXACIÓN
print(lista1[0:2])      # [1, 2] - SLICING desde pos0 hasta pos2 sin incluir la posicion 2

"""TERNARY - conditional expression: is a one-line shorthand for an if-else"""
edad = 20

# Sintaxis: valor_si_verdadero if condición else valor_si_falso
estado = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(estado)  # Mayor de edad

# Ejemplo con números
numero = 10
resultado = "Par" if numero % 2 == 0 else "Impar"
print(resultado)  # Par

""" unpacking operators (* and **) are used to extract multiple values from iterables (like lists or dictionaries)
 and distribute them into separate variables or function arguments"""
# Desempaquetado de tuplas/listas
a, b, c = (1, 2, 3)
print(a, b, c)  # 1 2 3

# Desempaquetado parcial
x, *resto = [1, 2, 3, 4, 5]
print(x)      # 1
print(resto)  # [2, 3, 4, 5]

# Desempaquetado en diccionarios
**diccionario = {"nombre": "Juan", "edad": 30}

"""F-STring: are string literals prefixed with f or F that allow expressions
 to be embedded directly inside curly braces {}"""
nombre = "Juan"
edad = 30

# F-string (Python 3.6+)
print(f"Mi nombre es {nombre} y tengo {edad} años")

# Expresiones dentro del f-string
print(f"Próximo año tendré {edad + 1} años")

# Formato de números
precio = 19.99
print(f"Precio: ${precio:.2f}")  # Precio: $19.99