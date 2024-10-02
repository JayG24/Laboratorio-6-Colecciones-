"""LISTAS"""
#clear(): Elimina todos los elementos de la lista.
lista = [1, 2, 3, 4]
lista.clear()
print(lista)  # Output: []

#copy(): Devuelve una copia superficial de la lista.
lista_1 = [1, 2, 3]
copia_lista = lista_1.copy()
print(copia_lista)  # Output: [1, 2, 3]

#index(): Devuelve el índice del primer elemento con el valor especificado.
lista_2 = [10, 20, 30, 20]
print(lista_2.index(20))  # Output: 1

#insert(): Inserta un elemento en una posición especificada.
lista_3 = [1, 2, 4]
lista_3.insert(2, 3)  # Inserta el número 3 en el índice 2
print(lista_3)  # Output: [1, 2, 3, 4]

#reverse(): Invierte el orden de los elementos de la lista.
lista_4 = [1, 2, 3]
lista_4.reverse()
print(lista_4)  # Output: [3, 2, 1]