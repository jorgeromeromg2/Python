print('='*30)
print('{:30}'.format('BANCO CASHBEST'))
print('='*30)
valor = int(input('Qual valor deseja sacar? R$ '))
total = valor
ced = 200
totced = 0
continuar = ''
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao \033[1:33mBANCO CASHBEST\033[m')