try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = num1 / num2
    print("El resultado es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")