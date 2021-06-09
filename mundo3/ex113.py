def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1:31mERRO! Digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt, KeyError):
            print('\033[1:31mERRO! Entrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1:31mERRO! Digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt, KeyError):
            print('\033[1:31mERRO! Entrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f"Você acabou de digitar o número {n1} inteiro e {n2} real.")