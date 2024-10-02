# Diccionario como cuentas múltiples

ccc = dict()  # Se crea un diccionario vacío llamado 'ccc'

ccc['Kevin'] = 1  # Se añade una clave 'Kevin' con el valor 1 al diccionario
ccc['Brayan'] = 1  # Se añade una clave 'Brayan' con el valor 1 al diccionario
print(ccc)  # Se imprime el diccionario completo: {'Kevin': 1, 'Brayan': 1}

ccc['Kevin'] = ccc['Kevin'] + 1  # Se incrementa el valor asociado a 'Kevin' en 1
print(ccc)  # Se imprime el diccionario actualizado: {'Kevin': 2, 'Brayan': 1}

print('Kevin' in ccc)  # Se verifica si 'Kevin' es una clave en el diccionario y se imprime el resultado (True)
