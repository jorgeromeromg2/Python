#----PALINDROMO------
'''print('Descubra se a palavra é um palíndromo.')
frase = str(input('Digite uma palavra: '))
frase = frase.upper().replace(' ', '')
if frase == frase[::-1]:
    print('A frase {} faz sentido mesmo invertida. '.format(frase))
else:
    print('A frase {} invertida não faz sentido.'.format(frase[::-1]))'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('A frase {} digitada é um palíndromo {}.'.format(junto, inverso))
else:
    print('A frase {} digitada não é um palíndromo {}.'.format(junto, inverso))