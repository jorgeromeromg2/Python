def escreva(msg):                           # A FUNÇÃO 'ESCREVA' CHAMA O COMANDO ESCREVA A BAIXO.
    tam = len(msg) + 5
    print('-' * tam)
    print(f'  {msg}')                       # ESCREVE NA TELA A QUANTIDADE DE VEZES QUE A FUNÇÃO ESCREVA APARECE
                                            # NO PRINCIPAL
    print('-' * tam)


escreva('JORGE LUIZ ROMERO MONTEIRO')
escreva('MAIRA ROBERTA TEIXEIRA MACIEL')
escreva('GUSTAVO MACIEL ROMERO')
escreva('GEOVANNA MACIEL ROMERO')
