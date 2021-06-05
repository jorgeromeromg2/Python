cont = 0
n = int(input('Quer ver a tabuada de qual valor? '))
while True:
    if n < 0:
        break
    for t in range(1, 11):
        r = n * t
        print(f'{n} X {t:2} = {r:2}')
    print('-=-' * 15)
    n = int(input('Quer ver a tabuada de qual valor agora? [-1 para encerrar] '))
    print('-=-' * 15)
    cont += 1
print(f'Tabuada encerrada. Foram feitas {cont} tabuadas.')