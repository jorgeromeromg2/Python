

def ano(data):
    res = data - 1993
    if 2010 <= data < 2011:
        print(f'Em {data} nos casamos. Você tinha seus {res} anos e foi quando nossa vida fez mais sentido do que '
              f'quando achávamos ja fazer no tempo de namoro e noivado.')
    elif 2011 <= data < 2012:
        print(f'{data}, foi mágico e difícil, você tinha {res}. Tempos em que a distancia provou o nosso amor. '
              f'Eu em Brasília, você em casa. Período que a internet que hoje temos nos aproximaria, mas '
              f'não tivemos esse privilégio. Parte dessa magia foi o direito que nos foi concedido de sermos pais.'
              f'Deus foi gracioso conosco.\033[1;97;41m Nosso amor estava se firmando!\033[m')
    elif data == 2012:
        print(f'{data}, período ainda com muitas provações, mas Deus estava conosco. Grandes experiências tivemos.'
              f' Deus então nos abençoa no ano seguinte com mais um filho! ')
    else:
        print(f'Sabe que não tenho uma memória muito boa! [kkkk] Depois do nascimento do Gustavo as coisas melhoraram.'
              f'Nossa vida tomou outro rumo, perspectiva e emadurecemos de tal forma que podemos dar certas uma para o '
              f'outro de quão fortes estamos e mais certos de que nosso amor é \033[1;32;107"PARA TODO SEMPRE" e '
              f'"AO INFINITO E ALÉM!"\033[m')


def musica(data):
    d = data
    import pygame
    cont = str(input('Quer ouvir uma música? [S/N]'))
    if cont in 'Ss':
        if 2010 < d < 2017:
            pygame.mixer.init()
            pygame.mixer.music.load('musicaB.mp3')
            pygame.mixer.music.play()
            input('Aumente o volume')
            return cont
        else:
            pygame.mixer.init()
            pygame.mixer.music.load('musicaA.mp3')
            pygame.mixer.music.play()
            input('Aumente o volume')
            return cont
    else:
        print('Infelizmente você não ouvirá uma música especial que preparei para você!')
