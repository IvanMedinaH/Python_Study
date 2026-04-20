
"""FOR"""
numero = 7

print(f"Tabla del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
# Imprime:
# Tabla del 7:
# 7 x 1 = 7
# 7 x 2 = 14
# ... y así hasta 7 x 10 = 70

"""IF-ELSE -FOR"""
numero = 17
es_primo = True

if numero < 2:
    es_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")
# Imprime: 17 es primo


"""FILTRAR LISTA"""
estudiantes = [
    {"nombre": "Juan", "calificacion": 85},
    {"nombre": "Ana", "calificacion": 92},
    {"nombre": "Carlos", "calificacion": 78},
    {"nombre": "Laura", "calificacion": 95}
]

for estudiante in estudiantes:
    nombre = estudiante["nombre"]
    calificacion = estudiante["calificacion"]
    
    if calificacion >= 90:
        estado = "Excelente"
    elif calificacion >= 80:
        estado = "Muy Bien"
    elif calificacion >= 70:
        estado = "Bien"
    else:
        estado = "Necesita mejorar"
    
    print(f"{nombre}: {calificacion} - {estado}")
# Imprime:
# Juan: 85 - Muy Bien
# Ana: 92 - Excelente
# Carlos: 78 - Bien
# Laura: 95 - Excelente