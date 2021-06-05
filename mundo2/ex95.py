from time import sleep
jogadores = []
lista = {}
gol = []
tot = chutes = 0
while True:
    lista["nome"] = str(input('Nome do Jogador: ')).capitalize()
    partidas = int(input('Quantidade de partidas: '))
    for p in range(1, partidas+1):
        chutes = (int(input(f'{" ":>5}Quantos gols na {p}ª partida : ')))
        tot += chutes
        gol.append(chutes)
    lista["gols"] = gol[:]
    lista["total"] = sum(gol)
    lista["partidas"] = partidas
    jogadores.append(lista.copy())
    gol.clear()
    continuar = str(input('Deseja continuar [S/N]: '))
    if continuar in 'Nn':
        break
print('==='*25)
print(f'{"cod":<13}', end='')
for k in lista.keys():
    print(f'{k:<15}', end='')
print()
print('---'*25)
for k, v in enumerate(jogadores):
    print(f'{k:>2}', end='')
    for d in v.values():
        print(f'{str(d):>16}', end='')
    print()
print('==='*25)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não exite jogador com esse código {busca}')
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}:')
        for i, g in enumerate(jogadores[busca]["gols"]):
            print(f'{" ":>5}No jogo {i+1} fez {g} gols.')
    print('-='*35)
print('<<< VOLTE SEMPRE >>>')