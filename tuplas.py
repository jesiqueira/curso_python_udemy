#tupla não pode ser modificado.
tupla = tuple
print(tupla)
tupla = ()
print(type(tupla))
# print(dir(tupla))
# print(help(tupla))
tupla = ('um',)
print(type(tupla))
print(tupla[0])
# tupla = 'novo' # não consegue add dados em uma tupla é imutavel

cores = ('verde', 'amarelo', 'azul', 'branco')
print(cores[0])
print(cores[-1])
print(cores[1])

print(cores.index('amarelo'))
print(cores.count('amarelo'))
print(len(cores))