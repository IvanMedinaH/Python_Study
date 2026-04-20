"""SEEK AND LOCATE"""
texto = "Hola Mundo"

# find() - encuentra la posición de una subcadena
print(texto.find("Mundo"))      # 5
print(texto.find("xyz"))        # -1 (no encontrado)

# index() - similar a find() pero lanza error si no existe
print(texto.index("Hola"))      # 0
# print(texto.index("xyz"))     # ❌ ValueError

# count() - cuenta cuántas veces aparece una subcadena
print(texto.count("o"))         # 2
print("banana".count("a"))      # 3

# startswith() - verifica si empieza con una cadena
print(texto.startswith("Hola")) # True
print(texto.startswith("Bye"))  # False

# endswith() - verifica si termina con una cadena
print(texto.endswith("Mundo"))  # True
print(texto.endswith("xyz"))    # False

"""TRANSFORM STRING"""
texto = "Hola Mundo"

# upper() - convierte a mayúsculas
print(texto.upper())            # HOLA MUNDO

# lower() - convierte a minúsculas
print(texto.lower())            # hola mundo

# capitalize() - primera letra mayúscula, el resto minúsculas
print(texto.capitalize())       # Hola mundo

# title() - primera letra de cada palabra mayúscula
print(texto.title())            # Hola Mundo

# swapcase() - intercambia mayúsculas y minúsculas
print("HoLa".swapcase())        # hOlA

# replace() - reemplaza una subcadena por otra
print(texto.replace("Mundo", "Python"))  # Hola Python

# strip() - elimina espacios al inicio y final
print("  Hola  ".strip())       # Hola

# lstrip() - elimina espacios al inicio
print("  Hola  ".lstrip())      # Hola  

# rstrip() - elimina espacios al final
print("  Hola  ".rstrip())      #   Hola


"""UNION && SPLIT"""
texto = "Hola,Mundo,Python"

# split() - divide la cadena en una lista
print(texto.split(","))         # ['Hola', 'Mundo', 'Python']
print("a,b,c".split(","))       # ['a', 'b', 'c']

# join() - une elementos de una lista en una cadena
lista = ['Hola', 'Mundo', 'Python']
print(" ".join(lista))          # Hola Mundo Python
print("-".join(lista))          # Hola-Mundo-Python

# rsplit() - divide de derecha a izquierda
print("a,b,c,d".rsplit(",", 2)) # ['a,b', 'c', 'd']

"""VALIDATION"""
# isdigit() - verifica si todos son dígitos
print("123".isdigit())          # True
print("12a".isdigit())          # False

# isalpha() - verifica si todos son letras
print("abc".isalpha())          # True
print("ab1".isalpha())          # False

# isalnum() - verifica si son letras o dígitos
print("abc123".isalnum())       # True
print("abc-123".isalnum())      # False

# isspace() - verifica si son espacios en blanco
print("   ".isspace())          # True
print(" a ".isspace())          # False

# islower() - verifica si está en minúsculas
print("hola".islower())         # True
print("Hola".islower())         # False

# isupper() - verifica si está en mayúsculas
print("HOLA".isupper())         # True
print("Hola".isupper())         # False


"""EXTRAS"""
texto = "Hola"

# len() - obtiene la longitud (también funciona con listas)
print(len(texto))               # 4

# format() - formatea una cadena
print("Hola {}".format("Juan")) # Hola Juan
print("Soy {} y tengo {}".format("Juan", 30))  # Soy Juan y tengo 30

# center() - centra el texto
print(texto.center(10, "-"))    # ---Hola---

# ljust() - alinea a la izquierda
print(texto.ljust(10, "-"))     # Hola------

# rjust() - alinea a la derecha
print(texto.rjust(10, "-"))     # ------Hola

# zfill() - rellena con ceros
print("42".zfill(5))            # 00042