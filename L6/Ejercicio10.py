# Se crea una lista llamada 't1' que contiene las letras 'a', 'b' y 'c'.
t1 = ['a', 'b', 'c']

# Se crea otra lista llamada 't2' que contiene las letras 'd' y 'e'.
t2 = ['d', 'e']

# Se añade cada elemento de la lista 't2' al final de la lista 't1' utilizando el método extend.
t1.extend(t2)

# Imprime la lista 't1' después de la extensión, que ahora es ['a', 'b', 'c', 'd', 'e'].
print(t1)
