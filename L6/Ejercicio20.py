# Diccionarios

bolsa = dict()  # Se crea un diccionario vacío llamado 'bolsa'

bolsa['dinero'] = 12  # Se añade una clave 'dinero' con el valor 12 al diccionario
bolsa['dulce'] = 3    # Se añade una clave 'dulce' con el valor 3 al diccionario
bolsa['papel'] = 75   # Se añade una clave 'papel' con el valor 75 al diccionario

# Se imprime el diccionario completo: {'dinero': 12, 'dulce': 3, 'papel': 75}
print(bolsa)  

# Se imprime el valor asociado a la clave 'dulce', que es 3
print(bolsa['dulce'])  

# Se actualiza el valor de 'dulce', sumando 2 al valor actual
bolsa['dulce'] = bolsa['dulce'] + 2  

# Se imprime el diccionario actualizado
print(bolsa)  