# Imprime un objeto de rango que genera números desde 0 hasta 3 (4 no incluido).
print(range(4))

# Inicia un bucle 'for' que itera sobre un rango de números desde 0 hasta 3.
for x in range(4):
    # Imprime el valor actual de 'x' en cada iteración.
    print(x)

# Se crea una lista llamada 'amigos' que contiene tres nombres.
amigos = ['Brayan', 'Kevin', 'Britany']

# Imprime un mensaje que indica cuántos amigos hay, convirtiendo la longitud de la lista en una cadena.
print("Tengo: " + str(len(amigos)) + " amigos")

# Imprime el mismo mensaje utilizando una f-string para insertar la longitud directamente.
print(f"Tengo: {len(amigos)} amigos")

# Imprime un objeto de rango que genera números desde 0 hasta la longitud de la lista 'amigos'.
print(range(len(amigos)))
