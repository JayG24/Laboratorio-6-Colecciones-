# Se crea una lista llamada 't' que contiene varios números enteros.
t = [9, 41, 12, 3, 74, 15]

# Imprime una porción de la lista 't' que incluye los elementos en los índices 1 y 2 (41 y 12).
print(t[1:3])

# Imprime una porción de la lista 't' que incluye los primeros cuatro elementos (hasta el índice 3).
print(t[:4])

# Imprime una porción de la lista 't' que incluye todos los elementos desde el índice 3 hasta el final.
print(t[3:])

# Imprime una copia completa de la lista 't'.
print(t[:])

# Se redefine la lista 't' con letras en lugar de números.
t = ['a', 'b', 'c', 'd', 'e', 'f']

# Sustituye los elementos en los índices 1 y 2 (b y c) por los nuevos elementos 'x' y 'y'.
t[1:3] = ['x', 'y']

# Imprime la lista 't' actualizada, que ahora es ['a', 'x', 'y', 'd', 'e', 'f'].
print(t)
