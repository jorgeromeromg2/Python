num1 = int(input('Escreva o primeiro número: '))
num2 = int(input('Escreva o segundo número: '))
if num1 > num2:
    print('O número {} é maior que {}.'.format(num1, num2))
elif num2 > num1:
    print('O número {} é maior que {}.'.format(num2, num1))
else:
    print('Os valores são iguais. Não existe maiores!')