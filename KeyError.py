try:
    datos = {"nombre": "Faustino", "edad": 25}
    print(datos["direccion"])
except KeyError:
    print("Error: La clave no existe en el diccionario.")
