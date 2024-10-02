# Diccionario como cuentas múltiples

contadores = dict()  # Se crea un diccionario vacío llamado 'contadores'
linea = input('Ingresa el texto: ')  # Se solicita al usuario que ingrese un texto
palabras = linea.split()  # Se divide el texto en palabras usando el método 'split()'

# Se itera sobre cada palabra en la lista 'palabras'
for palabra in palabras:
    contadores[palabra] = contadores.get(palabra, 0) + 1  # Se cuenta cada palabra usando 'get()' para obtener el conteo actual o 0

print("----------------------------------------------")
print(contadores.keys())  # Se imprimen las claves del diccionario (palabras únicas)
print("----------------------------------------------")
print(contadores.values())  # Se imprimen los valores del diccionario (conteos de cada palabra)
print("----------------------------------------------")
print(f'Total de palabras: {sum(contadores.values())}')  # Se imprime el total de palabras (suma de los valores)
print(f'Total de palabras no repetidas: {len(contadores)}')  # Se imprime el total de palabras únicas (número de claves)
