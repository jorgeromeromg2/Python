from time import sleep
rol = []
alunos = []
media = []
print('<<< \033[1:32:40mRELAÇÃO DE ALUNOS POR MÉDIA\033[m >>>')
semestre = int(input('Semestre: '))
while True:
    alunos.append(str(input('Nome: ')).capitalize())
    for s in range(1, semestre+1):
        alunos.append(float(input(f'Nota do {s}º semestre: ')))
    media.append(sum(alunos[1:])/semestre)
    rol.append(alunos[:])
    alunos.clear()
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
print('='*35)
print(f'\033[1m{"No.":<4}{"NOME":<10}{"MÉDIA":>8}\033[m')
print('='*35)
for c, r in enumerate(rol):
    print(f'{c + 1:<4}{r[0]:<10}{media[c]:>7.1f}')
    sleep(1)
while True:
    print('-' * 35)
    pos = int(input('Qual aluno deseja ver a nota? \033[1:32m999 para finalizar\033[m'))
    if pos <= len(rol):
        print(f'As notas do aluno \033[1:32m{rol[pos-1][0]}\033[m no {semestre}º semestre são {rol[pos-1][1:]}: ')
    if pos == 999:
        print(f'\033[1:31m{"FINALIZANDO":>5}...\033[m')
        sleep(2)
        break
print('<<< \033[1:32:40mVOLTE SEMPRE\033[m >>>')
