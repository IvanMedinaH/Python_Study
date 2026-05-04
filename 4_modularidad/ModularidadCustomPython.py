"""Archivo: calculadora.py"""

# En calculadora.py
"""encontraremos las funciones de: 
sumar
restar
el valor de Pi
"""

"""-----------------------------------------------------------"""

"""En otro archivo:"""

# Opción 1: Importar módulo
import modulos.calculadora as calculadora

resultado = calculadora.sumar(5, 3)  # 8
print(calculadora.PI)  # 3.14159

# Opción 2: Importar específico
from modulos.calculadora import sumar, restar

resultado = sumar(5, 3)  # 8
print(f"Resultado: {resultado}")
resultado = restar(10, 3)  # 7
print(f"Resultado: {resultado}")
# Opción 3: Importar todo (no recomendado, confuso)
from modulos.calculadora import *

resultado = sumar(5, 3)  # Funciona pero no es claro qué vienes
print(f"Resultado: {resultado}")