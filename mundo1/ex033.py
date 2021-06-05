reta1 = float(input('Digite a primeira reta: '))
reta2 = float(input('Digite a segunda reta: '))
reta3 = float(input('Digite a terceira reta: '))
if (reta1 + reta2 > reta3) and (reta2 + reta3 > reta1) and (reta1 + reta3 > reta2):
    print('Possui condição para ser um triângulo.')
else:
    print('Não possui condição para ser um triângulo.')