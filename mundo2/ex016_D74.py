from random import randint
lista = (randint(1, 10), randint(1, 10), randint(1, 10),
          randint(1, 10), randint(1, 10),)
print('Os valores sorteados foram:', end=' ')
for l in lista:
    print(f'{l}', end=' ')
print(f'\nO maior valor sorteado foi {max(lista)}')
print(f'O menor valor sorteado foi {min(lista)}')
print(sorted(lista))
print(sum(lista))
