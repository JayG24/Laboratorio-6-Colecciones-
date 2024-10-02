# Método split y operador in

abc = 'Con tres palabras'
# Se asigna una cadena de texto a la variable 'abc'

cosas = abc.split()
# Se divide la cadena en una lista de palabras utilizando el método 'split()', separando por espacios por defecto

print(cosas)
# Se imprime la lista resultante de dividir la cadena (['Con', 'tres', 'palabras'])

print(len(cosas))
# Se imprime la cantidad de elementos en la lista, que es el número de palabras (3)

print(cosas[0])
# Se imprime el primer elemento de la lista ('Con')

for w in cosas:
    print(w)
# Se itera sobre cada palabra en la lista 'cosas' e imprime cada una en una nueva línea ('Con', 'tres', 'palabras')
