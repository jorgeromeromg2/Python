'''lanche = ['hamburguer', 'suco', 'pizza', 'pudim'] #LISTA PRINCIPAL

lanche[2] = 'picole' #SUBSTITUI O ELEMENTO DA POSIÇÃO DESEJADA

lanche.append('uva') #ADICIONA NO FINAL DA LISTA

lanche.insert(2, 'cachorro quente') #ADICIONA NA POSIÇÃO DESEJADA

del lanche[0] #ELIMINA O INDICE E REPOSICIONA OS INDICES
if 'vinho' in lanche:
    lanche.remove('vinho')
else:
    print('Não foi possível adicionar')

lanche.pop(3) #USANDO O METODO POP SEM INDICE ELE REMOVE O ÚLTIMO ELEMENTO DA LISTA

valores = list(range(0, 10)) #METODO FOR APLICADO A LISTA CRIADA NA SEQUENCIA

valores = [0, 5, 2, 8, 9, 10, 23, 6] #LISTA CRIADA FORA DE ORDEM

valores.sort() #COLOCA EM ORDEM CRESCENTE

valores.sort(reverse=True) #COLOCA EM ORDEM DECRESCENTE
valores.sort(reverse=False) #COLOCA EM ORDEM CRESCENTE

print(len(valores))
print(valores)
print(len(lanche))
print(lanche)

from random import randint
cont = 0
valores = []
valores.append(randint(0, 10))
valores.append(randint(0, 10))
valores.append(randint(0, 10))
valores.append(randint(0, 10))
valores.append(randint(0, 10))
valores.append(randint(0, 10))
valores.append(randint(0, 10))
valores.append(randint(0, 10))
valores.append(randint(0, 10))
valores.append(randint(0, 10))
for c, v in enumerate(valores):
    cont += v
    print(f'Na posição {c} encontrei o valor {v}!')
print(f'Fim da lista. O valor máximo é {max(valores)} e mínimo é {min(valores)}')
print(f'A soma dos números é {cont}')
print(f'A lista é composta por {valores}')
print(f'Os valores em ordem são {sorted(valores)}')'''

'''valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(f'Os valores digitados são {sum(valores)}')

for p, v in enumerate(valores):
    print(f'O valor {v} está na posição {p+1}')
print('Fim da execução!')'''

#CONEXAO ENTRE AS LISTAS
a = [1, 2, 3, 4, 5]
b = a[:] #FOI CRIADO UMA COPIA DOS VALORES. ELA MANTEM A FIXO E ALTERA A LISTA B
b[2] = 6
print(f'Lista A: {a}')
print(f'Lista B: {b}')