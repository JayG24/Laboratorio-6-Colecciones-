#Delimitador
linea = 'Muchos         espacios'
etc = linea.split()
print(etc)
linea = 'primero;segundo;tercero'
cosa = linea.split()
print(cosa)
print(len(cosa))
cosa = linea.split(';')
print(cosa)
print(len(cosa))
