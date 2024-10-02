#Funciones nativas para listas
numlista = list()
while True :
    inp = input('Ingresa un número: ')
    if inp == 'fin' : break
    valor = float(inp)
    numlista.append(valor)

print(numlista)
promedio = sum(numlista) / len(numlista)
print('Promedio:', promedio)
