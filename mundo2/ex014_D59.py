'''#-----CALCULADORA-----
num1 = 0
num2 = 0
continuar = 0
#VARIAVEIS CONTADORAS
while continuar != 5: #ENQUANTO O VALOR FOR DIFERENTE DE 5 O PROGRAMA CONTINUA A EXECUTAR. 5 O PROGRAMA ENCERRA
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))
    continuar = int(input('[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR DO JOGO '
                          '>>>>> Escolha uma opção:')) #OPÇÕES PARA SER EXECUTADA
    if continuar == 1: #SOMA
        soma = num1 + num2
        print('A soma entre {} + {} = {}'.format(num1, num2, soma))
        print(10 * '-=-')
    if continuar == 2: #MULTIPLICAÇÃO
        mult = num1 * num2
        print('A multiplicação entre {} X {} = {}'.format(num1, num2, mult))
        print(10 * '-=-')
    if continuar == 3: #MAIOR NÚMERO DIGITADO
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('O maior número é {}'.format(maior))
        print(10 * '-=-')
    if continuar == 4: #OPÇÃO PARA DIGITAR UM NOVO NÚMERO
        continue
print('A calculadora foi encerrada.')'''

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('O valor {} + {} = {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O valor {} x {} = {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'. format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente.')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
print('Fim do programa. Volte sempre')
