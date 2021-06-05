'''pessoas = {'nome': 'Jorge', 'sexo': 'M', 'idade': 32}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
del pessoas['sexo']
pessoas['nome'] = 'Maira'
pessoas['peso'] = 65
for k, v in pessoas.items():
    print(k, v)'''
'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
for c, e in enumerate(brasil):
    print(c+1, e['sigla'])'''
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    #print(e['uf'], e['sigla'])
    #for v in e.values():
        #print(v, end=' ') #MOSTRA OS VALORES DO DICIONARIO
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}') #MOSTRA A CHAVE E O VALOR RELACIONADO