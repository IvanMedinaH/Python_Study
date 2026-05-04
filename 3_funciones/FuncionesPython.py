"""Una función es un bloque de código reutilizable 
que realiza una tarea específica.
"""
"""Una función es código reutilizable.
 La defines una sola vez, la llamas cuántas veces quieras."""
# Función sin entrada ni salida
def saludar():
    print("¡Hola!")

saludar()  # ¡Hola!
saludar()  # ¡Hola!



"""ESTRUCTURA BASICA"""
def nombre_funcion():
    # Código a ejecutar
    print("Hola desde una función")

# Llamar la función
nombre_funcion()
# Imprime: Hola desde una función

"""PARAMETROS"""
# Definir función con parámetro
def saludar(nombre):
    print(f"Hola, {nombre}")

# Llamar la función
saludar("Juan")
# Imprime: Hola, Juan

saludar("Ana")
# Imprime: Hola, Ana

"""MULTIPLES PARAMETROS"""
def suma(a, b):
    resultado = a + b
    print(f"{a} + {b} = {resultado}")

suma(5, 3)
# Imprime: 5 + 3 = 8

suma(10, 20)
# Imprime: 10 + 20 = 30

#---------------------------------------------------

"""RETURN"""
def multiplicar(a, b):
    resultado = a * b
    return resultado #<--

# La función retorna un valor
producto = multiplicar(4, 5)
print(producto)
# Imprime: 20

# Se puede usar directamente
print(multiplicar(7, 8))
# Imprime: 56

#---------------------------------------------------


"""RETURN MULTIPLE"""
def obtener_datos():
    nombre = "Juan"
    edad = 30
    ciudad = "Madrid"
    return nombre, edad, ciudad #<---

# Desempaquetar los valores retornados
nombre, edad, ciudad = obtener_datos()
print(f"{nombre}, {edad} años, {ciudad}")
# Imprime: Juan, 30 años, Madrid
#---------------------------------------------------


"""SIN RETURN EXPLICITO"""
def procesar_datos(numero):
    if numero > 0:
        print("Número positivo")
    else:
        print("Número negativo o cero")

resultado = procesar_datos(5)
print(resultado)
# Imprime:
# Número positivo
# None
#---------------------------------------------------

"""RETURN CONDICIONAL"""
def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

print(es_mayor_de_edad(25))
# Imprime: True

print(es_mayor_de_edad(15))
# Imprime: False


# Forma simplificada
def mayor_de_edad(edad):
    return edad >= 18

#---------------------------------------------------

"""DOCUMENTACION"""
def calcular_area_rectangulo(largo, ancho):
    """Calcula el área de un rectángulo.
    
    Parámetros:
    largo: la longitud del lado largo
    ancho: la longitud del lado corto
    
    Retorna:
    El área del rectángulo (largo * ancho)
    """
    area = largo * ancho
    return area

print(calcular_area_rectangulo(5, 3))
# Imprime: 15

# Ver la documentación
print(calcular_area_rectangulo.__doc__)