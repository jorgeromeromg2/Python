print('=='*20)
print('CADASTRO DE PESSOAS [IDADE E SEXO]')
print('=='*20)
idade = idadeMaior = idadeMenor = masc = fem = 0
totFem = 0
sexo = continuar = ''
while True:
    idade = int(input('Idade: '))
    while idade <= 0:
        idade = int(input('Idade incorreta. Digite a idade: '))
    if idade >= 18:
        idadeMaior += 1
    else:
        idadeMenor += 1
    sexo = str(input('Sexo[M/F]: ')).strip()[0]
    while sexo not in 'MmFf':
        sexo = str(input('Sexo inválido. Digite o sexo [M/F]: ')).strip()[0]
    if sexo in 'Mm':
        masc += 1
    if sexo in 'Ff':
        fem += 1
    if sexo in 'Ff' and idade > 18:
        totFem += 1
    print('--' * 20)
    continuar = str(input('Deseja continuar[S/N]:')).strip()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Valor incorreto. Deseja continuar[S/N]:')).strip()[0]
    if continuar in 'Nn':
        break
print('==='*5, 'FIM DE CADASTRO', '==='*5)
print(f'Total de pessoas maiores de \033[2:32m18 anos\033[m é {idadeMaior} ')
print(f'Total de pessoas menores de \033[2:31m18 anos\033[m é {idadeMenor} ')
print(f'Temos ao todo \033[1:34m{masc} homens\033[m e \033[1:35m{fem} mulheres\033[m.')
if totFem <= 1:
    print(f'E ao {totFem} mulher com \033[2:32mmais de 18 anos\033[m')
else:
    print(f'E ao {totFem} mulheres com \033[2:32mmais de 18 anos\033[m')