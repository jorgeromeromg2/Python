print('DADOS SOBRE PESO')
consultorio = []
pessoas = []
maior = menor = 0
while True:
    pessoas.append(str(input('Nome: ').capitalize()))
    pessoas.append(float(input('Peso: ')))
    if len(consultorio) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    consultorio.append(pessoas[:]) #CRIA UMA CÓPIA
    pessoas.clear()
    continuar = (str(input('Quer continuar? [S/N] ').strip()))
    if continuar in 'Nn':
        break
print('==='*30)
print(f'Foram cadastrados {len(consultorio)} pessoas')
print(f'O maior peso foi de {maior:.2f} Kg do ', end='')
for p in consultorio:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso foi de {menor:.2f} Kg do ', end='')
for p in consultorio:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')

