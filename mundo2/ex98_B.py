from time import sleep


def contador(i, f, p):                                  # CHAMA O PROGRAMA PRINCIPAL
    if p < 0:                                           # CONDIÇÃO CASO USUÁRIO DIGITE UM NÚMERO NEGATIVO
        p *= -1
    if p == 0:                                          # CONDIÇÃO CASO USUÁRIO DIGITE O ZERO
        p = 1
    print('==='*10)
    print(f'Contagem de {i} até {f} de {p} em {p}.')    # IMPRIME NA TELA A CONTAGEM
    sleep(1.5)
    if i < f:                                           # CONDIÇÃO PARA O 'INÍCIO' MENOR DO QUE O 'FIM'
        cont = i
        while cont <= f:
            sleep(0.5)
            print(f'{cont} ', end='', flush=True)
            cont += p
        print('FIM')
    else:                                               # CONDIÇÃO PARA O 'INÍCIO MAIOR DO QUE O 'FIM'
        cont = i
        while cont >= f:
            sleep(0.5)
            print(f'{cont} ', end='', flush=True)
            cont -= p
        print('FIM')


# Programa Principal
contador(1, 10, 1)
contador(10, 1, 2)
print('=='*10)
print('Agora é sua sua vez de personalizar a contagem!')    # INPUT PARA PERSONALIZAR A CONTAGEM
ini = int(input('\33[1mInício: \033[m'))
fim = int(input('\33[1mFim: \033[m'))
inter = int(input('\33[1mIntervalo: \033[m'))
contador(ini, fim, inter)
