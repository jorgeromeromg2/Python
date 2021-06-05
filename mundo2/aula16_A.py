#TUPLAS
'''lanche = ('') [] {} # TUPLA / LISTA / DICIONARIO'''

lanche = ('Hamburguer', 'Pizza', 'Batata Frita', 'Suco', 'Maçã', 'Refrigerante')

'''#FORMAS DE CONTAR A TUPLA
for c in range(3, len(lanche)):
    print(f'Comi {lanche[c]}. Que está na posição {c} da tupla.')
    
for c in lanche:
    print(f'Comi {c}')

for pos, c in enumerate(lanche):
    print(f'Comi {c}. Que está na posição {pos}.')

print(sorted(lanche)[0]) #COLOCA EM ORDEM A TUPLA

print('Estou satisfeito!')
print('Comi bastante!')'''

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(f'A lista: {c}')
print(f'O número 5 aparece: {c.count(5)} vezes.') #mostra quantas vezes aparece o número solicitado
print(f'O número 5 aparece na posição {c.index(5, 0), c.index(5, 1)}') #mostra a posição do número solicitado (variavel, deslocamento)
print(f'O número que aparece na primeira posição é o {c[0]}')
pessoa = ('Jorge', 32, 'M', 85)
print(pessoa)