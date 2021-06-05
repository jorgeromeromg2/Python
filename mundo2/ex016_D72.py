n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
continuar = ''
numero = 0
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    while numero < 0 or numero > 20:
        numero = int(input('O número não correspondente ao solicitado. Digite novamente um número entre 0 e 20: '))
    print(f'Você digitou o número \033[1:32m{n[numero]}\033[m')
    continuar = str(input('Deseja continuar [S]Sim ou [N]Não: ')).strip().upper()
    if continuar in 'Nn':
        break
print('Fim da execução.')