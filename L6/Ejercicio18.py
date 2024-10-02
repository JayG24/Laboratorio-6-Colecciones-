def calcular_maximo_minimo():
    numeros = []  # Inicializamos una lista vacía para almacenar los números

    while True:
        entrada = input("Ingresa un número (o 'fin' para terminar): ")  # Pedimos un número al usuario
        if entrada.lower() == 'fin':  # Comprobamos si el usuario quiere finalizar
            break
        try:
            numero = float(entrada)  # Convertimos la entrada a un número (flotante)
            numeros.append(numero)  # Añadimos el número a la lista
        except ValueError:
            print("Por favor, ingresa un número válido.")  # Manejo de errores para entradas no numéricas

    if numeros:  # Verificamos si la lista no está vacía
        print(f"Números ingresados: {numeros}")  # Imprimimos la lista de números
        maximo = max(numeros)  # Calculamos el máximo
        minimo = min(numeros)  # Calculamos el mínimo
        print(f"Máximo: {maximo}")  # Imprimimos el máximo
        print(f"Mínimo: {minimo}")  # Imprimimos el mínimo
    else:
        print("No se ingresaron números.")

# Llamamos a la función
calcular_maximo_minimo()