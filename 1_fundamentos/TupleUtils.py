""""""
tupla = (1, 2, 3, 2, 4, 2)

# count() - cuenta cuántas veces aparece un elemento
print(tupla.count(2))           # 3
print(tupla.count(1))           # 1

# index() - encuentra la posición del primer elemento en la tupla
print(tupla.index(2))           # 1
print(tupla.index(4))           # 4

# len() - obtiene la cantidad de elementos
print(len(tupla))               # 6

# min() y max() - encuentra menor y mayor valor
tupla = (5, 2, 8, 1, 9)
print(min(tupla))               # 1
print(max(tupla))               # 9

# sum() - suma todos los elementos
print(sum(tupla))               # 25

# sorted() - retorna una lista ordenada
print(sorted(tupla))            # [1, 2, 5, 8, 9]

# in - verifica si un elemento existe
print(2 in tupla)               # True
print(99 in tupla)              # False