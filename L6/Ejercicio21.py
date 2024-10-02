# Listas VS Diccionarios

lst = list()  # Se crea una lista vacía llamada 'lst'

lst.append(21)  # Se añade el valor 21 a la lista
lst.append(183)  # Se añade el valor 183 a la lista
print(lst)  # Se imprime la lista completa: [21, 183]

lst[0] = 23  # Se actualiza el primer elemento de la lista, cambiándolo de 21 a 23
print(lst)  # Se imprime la lista actualizada: [23, 183]

ddd = dict()  # Se crea un diccionario vacío llamado 'ddd'

ddd['edad'] = 21  # Se añade una clave 'edad' con el valor 21 al diccionario
ddd['curso'] = 182  # Se añade una clave 'curso' con el valor 182 al diccionario
print(ddd)  # Se imprime el diccionario completo: {'edad': 21, 'curso': 182}

ddd['edad'] = 23  # Se actualiza el valor de 'edad', cambiándolo de 21 a 23
print(ddd)  # Se imprime el diccionario actualizado: {'edad': 23, 'curso': 182}
