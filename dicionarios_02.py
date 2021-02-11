pessoa = {'nome': 'Edmar', 'idade': 44, 'cursos': ['React', 'Python']}
pessoa['idade'] = 36
pessoa['cursos'].append('Angular')
print(pessoa)
print(pessoa.pop('idade'))
print(pessoa)
pessoa.update({'idade': 40, 'sexo': 'M'})
print(pessoa)
del pessoa['cursos']
print(pessoa)
pessoa.clear()
print(pessoa)