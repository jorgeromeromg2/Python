from time import sleep
lista = {}                                                              #DICIONARIO
gols = []                                                               #LISTA COM A VARIAVEL CHUTES
tot = 0                                                                 #VARIAVEL CONTADORA
lista["nome"] = str(input('Nome do Jogador: ')).capitalize()            #INPUT DO NOME ADICIONANDO AO DICIONÁRIO
partidas = int(input('Quantidade de partidas: '))                       #INPUT DAS PARTIDAS
for p in range(1, partidas+1):                                          #FOR DA QUANTIDADE DE PARTIDAS
    chutes = (int(input(f'{" ":>5}Quantos gols na partida {p}: ')))     #INPUT DOS GOLS QUE SÃO ADICIONADOS NA LISTA
    tot += chutes                                                       #CONTADOR SOMATORIO DE GOLS
    gols.append(chutes)                                                 #INCLUINDO NA LISTA GOLS
lista["gols"] = gols                                                    #INCLUINDO A LISTA GOLS NO DICIONÁRIO
lista["total"] = tot # ou sum(gols)                                     #INCLUINDO A LISTA TOTAL DE GOLS NO DICIONARIO
print('---'*20)
print(lista)                                                            #IMPRIME A LISTA
print('---'*20)
for k, v in lista.items():                                              #FOR DA CHAVE E VALOR DENTRO DA LISTA
    print(f'O campo {k} tem o valor {v}')                               #VALOR E LISTA IMPRESSOS EM TELA
    sleep(1)                                                            #TIME PARA APRESENTAR PROXIMA RELACAO
print('==='*20)
print(f'O jogador {lista["nome"]} jogou {len(lista["gols"])} partidas.')
print('==='*20)
for p, g in enumerate(gols):
    print(f'{"=>":>5} Na partida {p+1}, fez {g} gols')
    sleep(1)
print(f'Foi um total de {tot} gols')