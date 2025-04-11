try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = num1 / num2
    print("El resultado es:", resultado)
except ZeroDivisionError:
    print("Error: División por cero.")
except ValueError:
    print("Error: Entrada no válida. Debes ingresar números.")
