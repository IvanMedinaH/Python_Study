"""IF"""
edad = 20

# if simple
if edad >= 18:
    print("Eres mayor de edad")

"""IF ELSE"""
edad = 15

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
# Imprime: Eres menor de edad

"""IF-ELIF-ELSE"""
calificacion = 75

if calificacion >= 90:
    print("A - Excelente")
elif calificacion >= 80:
    print("B - Muy Bien")
elif calificacion >= 70:
    print("C - Bien")
elif calificacion >= 60:
    print("D - Aceptable")
else:
    print("F - No aprobado")
# Imprime: C - Bien


"""NESTED"""
edad = 25
tiene_licencia = True

if edad >= 18:
    if tiene_licencia:
        print("Puedes conducir")
    else:
        print("Debes obtener una licencia")
else:
    print("Eres muy joven para conducir")
# Imprime: Puedes conducir

"""LOGIC OPERATORS"""
edad = 25
tiene_dinero = True

# AND - ambas condiciones deben ser verdaderas
if edad >= 18 and tiene_dinero:
    print("Puedes comprar un carro")
# Imprime: Puedes comprar un carro

# OR - al menos una condición debe ser verdadera
es_fin_semana = False
es_festivo = True
if es_fin_semana or es_festivo:
    print("¡No hay que trabajar!")
# Imprime: ¡No hay que trabajar!

# NOT - invierte la condición
es_lluvioso = False
if not es_lluvioso:
    print("Puedes salir a jugar")
# Imprime: Puedes salir a jugar

"""TERNARY"""
edad = 20

# Sintaxis: valor_si_verdadero if condición else valor_si_falso
estado = "Mayor" if edad >= 18 else "Menor"
print(estado)
# Imprime: Mayor

# Otro ejemplo
numero = 10
tipo = "Par" if numero % 2 == 0 else "Impar"
print(tipo)
# Imprime: Par
