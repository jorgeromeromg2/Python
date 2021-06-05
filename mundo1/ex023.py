# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
'''
#------EXERCICIO 022 -----

nome = input('Digite seu nome: ').strip()
print('Seu nome todo em maiúsculo é: {}'.format(nome.upper()))
print('Seu nome todo em minúsculo é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem: {} letras '.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))'''

'''
#------ EXERCICIO 023 -------
numero = int(input('Digite um número: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))'''

'''#------ EXERCICIO 024 --------
cidade = str(input('Digite o nome da cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')'''

'''
#----- EXERCICIO 025 ----------
nome = str(input('Digite o nome completo: ')).strip()
#print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
nome1 = 'silva' in nome.lower()
if nome1:
    print('Você é um Silva')
else:
    print('Você não é um Silva')
'''

#----- EXERCICIO 026 --------

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra "A" aparece {} vezes.'.format(frase.count('A')))
print('A letra "a" aparece na primeira posição em: {}'.format(frase.find('A')+1))
print('A letra "a" aparece na última posição em: {}.'.format(frase.rfind('A')+1))


#------EXERCICIO 27------

'''nome = str(input('Digite seu nome completo: ')).strip()
nome1 = nome.split()
print('Seu primeiro nome é {}'.format(nome1[0]))
print('Seu último nome é {}'.format(nome1[len(nome1)-1]))'''
