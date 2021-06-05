jogadores = [{'nome': 'Jorge', 'gols': [0, 1], 'Total': 1}, {'nome': 'Maira', 'gols': [0, 0], 'Total': 0}]
gol = {}
print('cod', end='')
for i in jogadores:
    for k in i.keys():
        print(f'{k:<15}', end='')
print()
print('---'*30)
for k, v in enumerate(jogadores):
    print('')
