def obtener_numero():
    while True:
        try:
            numero = float(input("Introduce un número: "))
            return numero
        except ValueError:
            print("¡Eso no es un número válido! Inténtalo de nuevo.")

def encontrar_mayor(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print("Por favor ingresa tres números.")
numero1 = obtener_numero()
numero2 = obtener_numero()
numero3 = obtener_numero()


mayor = encontrar_mayor(numero1, numero2, numero3)
print(f"El número mayor es: {mayor}")
