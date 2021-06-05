def metragem(l, c):
    a = l * c  # área
    p = (2 * l) + (2 * c)  # perímetro
    print(f'A área de um terreno {l} x {c} é de {a}m².')
    print(f'O perímetro de um terreno {l} x {c} é de {p}m.')


# Programa Principal - este bloco é impresso na tela. A função é executado no comando 'metragem' e
# logo é impresso sua execução;
print('Controle de Terreno')
print('-'*20)
largura = float(input('\033[1mLARGURA (m):\033[m '))
comprimento = float(input('\033[1mCOMPRIMENTO (m):\033[m '))
metragem(largura, comprimento)
