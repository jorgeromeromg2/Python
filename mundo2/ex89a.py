ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('='*35)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('='*35)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Qual aluno deseja mostrar nota? (999 interrompe)'))
    if opc <= len(ficha)-1:
        print(f'As notas de {ficha[opc][0]} são {ficha[opc][1]}.')
    if opc == 999:
        print('FINALIZANDO...')
        break
print('<<< \033[2:32:45mVOLTE SEMPRE\033[m >>>')