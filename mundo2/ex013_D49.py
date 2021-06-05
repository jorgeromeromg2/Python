#-----TABUADA--------
print('Realize operações de 1 à 10')
opcao = int(input('''[1] ADIÇÃO
[2] SUBTRAÇÃO
[3] MULTIPLICAÇÃO
[4] DIVISÃO
Escolha a opção que deseja verificar: '''))
numero = int(input('Digite o número que deseja consultar: '))
if opcao == 1:
    for c in range(0, 10+1):
        resultado = c + numero
        print(c, '+', numero, '=', resultado)
elif opcao == 2:
    for c in range(0, 10+1):
        resultado = c - numero
        print(c, '-', numero, '=', resultado)
elif opcao == 3:
    for c in range(0, 10+1):
        resultado = c * numero
        print(c, 'x', numero, '=', resultado)
elif opcao == 4:
    for c in range(0, 10+1):
        resultado = c / numero
        print(c, '/', numero, '=', resultado)
else:
    print('Opção inválida! Tente novamente.')
print('fim')
