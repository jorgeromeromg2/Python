from time import sleep
cadastro1 = {}
cadastro2 = []
soma = 0
maior = 0
while True:
    cadastro1["nome"] = str(input('Nome: ')).capitalize()
    cadastro1["sexo"] = str(input('Sexo [M/F]: ')).capitalize()
    while cadastro1["sexo"] not in 'MmFf':
        cadastro1["sexo"] = str(input('\033[1:35mERRO!\033[m Por favor, digite apenas M ou F: '))
    cadastro1["idade"] = int(input('Idade: '))
    cadastro2.append(cadastro1.copy())
    continuar = str(input('Deseja continuar [S/N]: '))
    while continuar not in 'NnSs':
        continuar = str(input('\033[1:33mERRO!\033[m Por favor, responda apenas S ou N: '))
        if continuar in 'Nn':
            break
    if continuar in 'Nn':
        break
for k, v in enumerate(cadastro2):
    soma += v["idade"]
media = soma/len(cadastro2)
sleep(1)
print(f'A) Ao todo temos {len(cadastro2)} pessoas cadastradas.')
sleep(1)
print(f'B) A média de idade é de {media:.2f} anos.')
sleep(1)
print(f'C) As mulheres cadastradas foram: ', end='')
for s in cadastro2:
    if s["sexo"] in 'Ff':
        print(s["nome"], end='; ')
sleep(1)
print()
print(f'D) A lista das pessoas que estão acima da média:')
for c in cadastro2:
    if c["idade"] >= media:
        sleep(1)
        for k, v in c.items():
            print(f'{" ":>5}{k} = {v}; ', end='')
        print()
print('<<< ENCERRADO >>>')