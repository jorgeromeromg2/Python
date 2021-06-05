palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
            'MERCADO', 'PROGRAMADOR', 'FUTURO')
for pos in palavras: #O FOR PARA LISTAR AS PALAVRAS
    print(f'\nNa palavra {pos:<2} temos as vogais: ', end=' ') #PRINT DE CADA VALOR EM LINHA
    for letra in pos: #FOR PARA LISTAR AS VOGAIS EM CONDIÇÃO
        if letra.upper() in 'AEIOU': #CONDIÇÃO PARA AS VOGAIS
            print(f'{letra:<1.5}', end=' ') #FORMATAÇÃO DO PRINT COM ESPAÇOS
