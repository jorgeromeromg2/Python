aluno = dict()
aluno['Nome'] = str(input('Nome: ')).capitalize()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno["Média"] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno["Média"] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('==='*15)
for k, v in aluno.items():
    print(f'{"-":>5} {k} é igual a {v}')
