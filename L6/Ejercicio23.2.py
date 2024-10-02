#Diccionario como cuentas múltiples
contadores = dict()
nombres = ['Kevin', 'Brayan', 'Kevin', 'Jan', 'Brayan']
for nombre in nombres :
    contadores[nombre] = contadores.get(nombre,0) + 1
print(contadores)
