print('=='*30)
titulo = 'LISTAGEM DE PREÇOS'
print(titulo.center(60))
print('=='*30)
lista = ('Lápis', 1.75,
         'Borracha', 2.00,
         'Caderno', 15.90,
         'Estojo', 25.00,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livros', 34.90)#LISTA COM 18 VALORES

for pos in range(0, len(lista)):#LEN() É O TAMANHO DA LISTA
    # ESTE PRIMEIRO É REFERENTE A DIVISÃO DA POSIÇÃO NA LISTA. EX.: 0, 2, 4, 6, 8... É A POSIÇÃO DOS NOMES
    if pos % 2 == 0:
        #LISTA[POS] É UMA FORAM DE PRINTAR O NOME NA POSIÇÃO
        print(f'{lista[pos]:.<50}', end='')#ADICIONA ESPAÇOS E OS PONTOS DEPOIS DO 'FOR' DA LISTA
    else:
        # ESTE É REFERENTE A DIVISÃO DA POSIÇÃO NA LISTA IMPAR. EX.: 1, 3, 5, 7, 9... É A POSIÇÃO DOS VALORES
        print(f'R${lista[pos]:>8.2f}')#ADICIONA O R$ E DUAS CASAS DECIMAIS.
