'''n = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passos: '))
for c in range(n, f+1, p):
    print(c)
print('Fim!')'''

s = 0
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório dos números digitados é: {}'
      .format(s))

