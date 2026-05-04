"""Son funciones anónimas (sin nombre) en una sola línea."""
# Función normal
def doblar(x):
    return x * 2

# Equivalente con lambda
doblar = lambda x: x * 2
print(f"doblar valor {doblar(15)}")  # 10

# Lambda sin asignar a variable (rara vez)
resultado = (lambda x: x ** 2)(5)  # 25
print(f"resultado: {resultado}")


"""MAP FILTER SORTED"""
numeros = [1, 2, 3, 4, 5]

# map: Transformar cada elemento
duplicados = list(map(lambda x: x * 2, numeros))
print(duplicados)  # [2, 4, 6, 8, 10]

# filter: Seleccionar solo algunos
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4]

# sorted: Ordenar por algo
personas = [
    {"nombre": "Juan", "edad": 25},
    {"nombre": "Ana", "edad": 20},
]
ordenadas = sorted(personas, key=lambda p: p["edad"])
# [{"nombre": "Ana", "edad": 20}, {"nombre": "Juan", "edad": 25}]