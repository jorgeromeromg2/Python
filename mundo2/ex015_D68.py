from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*20)
jogador = total = 0
computador = vit = der = 0
continuar = ''
nome = str(input('Qual é o seu nome? ')).strip().upper()
while True:
    computador = randint(0, 10)
    jogador = int(input('Diga um valor entre 0 e 10: '))
    valor = str(input('[P]Par ou [I]Ímpar? ')).strip()[0]
    total = jogador + computador
    while valor not in 'PpIi':
        valor = str(input('Dados incorreto. Digite [P]Par ou [I]Ímpar: ')).strip()[0]
    print('-' * 30)
    if valor in 'Pp' and total % 2 == 0:
        print(f'\033[2:32m{nome}\033[m, você jogou {jogador} e o computador {computador}. '
              f'O resultado foi {total} que é PAR.')
        print('Você \033[2:32mGANHOU\033[m')
        vit += 1
    if valor in 'Ii' and total % 2 != 0:
        print(f'\033[2:32m{nome}\033[m, você jogou {jogador} e o computador {computador}. '
              f'O resultado foi {total} que é IMPAR.')
        print('Você \033[2:32mGANHOU\033[m')
        vit += 1
    if valor in 'Pp' and total % 2 != 0:
        print(f'\033[2:31m{nome}\033[m, você jogou {jogador} e o computador {computador}. '
              f'O resultado foi {total} que é IMPAR.')
        print('Você \033[2:31mPERDEU\033[m')
        der += 1
    if valor in 'Ii' and total % 2 == 0:
        print(f'\033[2:31m{nome}\033[m, você jogou {jogador} e o computador {computador}. '
              f'O resultado foi {total} que é PAR.')
        print('Você \033[2:31mPERDEU\033[m')
        der += 1
    continuar = str(input('Deseja continuar [S] Sim ou [N] Não? ')).strip()[0]
    while continuar not in 'NnSs ':
        continuar = str(input('Valor incorreto. Digite [S] Sim ou [N] Não: ')).strip().upper()[0]
    if continuar in 'Ss':
        continue
    else:
        break
#print(f'Você perdeu depois de {cont} jogadas.')
if vit and der <= 1:
    print(f'{nome}, você \033[2:32mvenceu {vit} vez\033[m e \033[2:31mperdeu {der} vez\033[m.')
else:
    if vit > 1 and der > 1:
        print(f'{nome}, você \033[2:32mvenceu {vit} vezes\033[m e \033[2:31mperdeu {der} vezes\033[m.')
    elif der > 1:
        print(f'{nome}, você \033[2:32mvenceu {vit} vez\033[m e \033[2:31mperdeu {der} vezes\033[m.')
    elif vit > 1:
        print(f'{nome}, você \033[2:32mvenceu {vit} vezes\033[m e \033[2:31mperdeu {der} vez\033[m.')

