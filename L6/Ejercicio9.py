#Método append
t = ['a', 'b', 'c']
print(t)
t.append('d')
print(t)

#Crear lista desde cero
cosas = list()
cosas.append('libro')
cosas.append(99)
print(cosas)
cosas.append('galleta')
print(cosas)
cosas.append('galleta', 'chorizo')
print(cosas)
ncosas = ['galleta', 'chorizo']
cosas.append(ncosas)
print(cosas)
