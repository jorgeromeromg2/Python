def fatorial(n, show=False):
    from time import sleep
    f = 1
    for c in range(n, 0, -1):
        sleep(0.5)
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa Principal
n1 = int(input('Digite um número para saber o fatorial: '))
print(fatorial(n1, show=True))
print('<<< Fim da execução >>>!')