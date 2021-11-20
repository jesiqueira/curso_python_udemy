#acessar elementos de uma lista.
lista = [1, 5, 'Rebeca', 'Guilherme', 3.12121]
# print(lista.index('Guilherme'))
# print(lista[2])
# print(lista[0])
# print(lista[4])
print('Rebeca' in lista)
print('Pedo' not in lista)
print(lista[-1])
print(lista[-5])

lista = ['Ana', 'Lia', 'Rui', 'Paulo', 'Dani']
print(lista[1:3])
print(lista[1:-1])
print(lista[1:])
print(lista[1:])
print(lista[:-1])
print(lista[:])
print(lista[::2])
print(lista[::-1])
del lista[2]
print(lista)
del lista[1:]
print(lista)