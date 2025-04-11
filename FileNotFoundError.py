try:
    archivo = open("archivo.txt", "r")
    print("El archivo existe.")
    archivo.close()
except FileNotFoundError:
    print("El archivo no existe. Se va a crear uno nuevo.")
    archivo = open("archivo.txt", "w")
    archivo.write("Este archivo fue creado porque no existía.")
    archivo.close()

