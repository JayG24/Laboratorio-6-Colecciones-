# Se crea una lista llamada 't' que contiene las letras 'd', 'c', 'e', 'b' y 'a'.
t = ['d', 'c', 'e', 'b', 'a']

# Imprime la lista original 't' antes de ordenarla.
print(t)

# Ordena la lista 't' en orden alfabético utilizando el método sort().
t.sort()

# Imprime la lista 't' después de ordenarla, que ahora será ['a', 'b', 'c', 'd', 'e'].
print(t)

# Ordena la lista 't' en orden alfabético inverso (de Z a A) utilizando el método sort() con reverse=True.
t.sort(reverse=True)

# Imprime la lista 't' después de ordenarla en orden inverso, que ahora será ['e', 'd', 'c', 'b', 'a'].
print(t)
