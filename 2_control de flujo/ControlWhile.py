contador = 1

while contador <= 5:
    print(contador)
    contador += 1
# Imprime: 1, 2, 3, 4, 5

# Otro ejemplo
contraseña_correcta = "python123"
intento = ""

while intento != contraseña_correcta:
    intento = input("Ingresa la contraseña: ")
    if intento == contraseña_correcta:
        print("¡Acceso concedido!")
    else:
        print("Contraseña incorrecta, intenta de nuevo")