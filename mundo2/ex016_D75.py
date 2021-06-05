num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'Em ordem são {sorted(num)}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
print(f'O valor 3 apareceu na {num.index(3)+1} posição.')
print(f'Os números pares são: ', end='')
for p in num:
    if p % 2 == 0:
        print(p, end=' ')
print(f'\nO números ímpares são: ', end='')
for i in num:
    if i % 2 != 0:
        print(i, end=' ')
