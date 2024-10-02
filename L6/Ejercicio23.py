# Diccionario como cuentas múltiples

contadores = dict()  # Se crea un diccionario vacío llamado 'contadores'
nombres = ['Kevin', 'Brayan', 'Kevin', 'Jan', 'Brayan']  # Se define una lista de nombres

# Se itera sobre cada nombre en la lista 'nombres'
for nombre in nombres:
    if nombre not in contadores:  # Si el nombre no está en el diccionario
        contadores[nombre] = 1  # Se añade la clave con el valor 1
    else:  # Si el nombre ya está en el diccionario
        contadores[nombre] = contadores[nombre] + 1  # Se incrementa su valor en 1

print(contadores)  # Se imprime el diccionario con los conteos de cada nombre
