def ficha(jog='<desconhecido>', gol=0):
    """
    A função ficha chama os inputs N e G verificados nas condições no programa principal.
    :param jog: recebe o nome do jogador depois de avaliada a condição se vazio
    :param gol: recebe a quantidade de gols digitada depois de avaliada
    :return: imprime a função verificada
    """
    return f'O jogador {jog} fez {gol} gol(s) no campeonato.'


# Programa Principal
som = 0
n = str(input('Nome do Jogador: ')).capitalize()
j = int(input('Quantos jogos: '))
for c in range(1, j+1):
    g = str(input(f'Número de Gols no {c}º jogo: '))
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    som += int(g)
if n.strip() == '':
    print(ficha(gol=som))
else:
    print(ficha(n, som))
# help(ficha)
