new = input("Ingrese una patente (Sin puntos ni espacios. Ej: ABC123):")
alfa_mayus = [chr(i) for i in range(65, 91)]
# Validar si es una patente

if len(new) != 6:
    print("La patente ingresada no es valida")
