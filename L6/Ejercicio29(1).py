"""DICCIONARIOS""" 
#clear(): Elimina todos los elementos del diccionario.
diccionario = {'a': 1, 'b': 2}
diccionario.clear()
print(diccionario)  # Output: {}

#copy(): Devuelve una copia superficial del diccionario.
diccionario_1 = {'a': 1, 'b': 2}
copia_diccionario = diccionario_1.copy()
print(copia_diccionario)  # Output: {'a': 1, 'b': 2}

#fromkeys(): Crea un nuevo diccionario con claves de un iterable y valores predeterminados.
claves = ('a', 'b', 'c')
diccionario_2 = dict.fromkeys(claves, 0)
print(diccionario_2)  # Output: {'a': 0, 'b': 0, 'c': 0}

#popitem(): Elimina y devuelve el último par clave-valor insertado.
diccionario_3 = {'a': 1, 'b': 2, 'c': 3}
print(diccionario_3.popitem())  # Output: ('c', 3)

#setdefault(): Devuelve el valor de una clave. Si la clave no existe, inserta la clave con un valor predeterminado.
diccionario_4 = {'a': 1}
print(diccionario_4.setdefault('b', 2))  # Output: 2
print(diccionario_4)  # Output: {'a': 1, 'b': 2}

