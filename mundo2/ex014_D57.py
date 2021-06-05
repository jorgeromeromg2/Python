#-----DEFININDO A QUANTIDADE DE GENEROS
'''sexo = 0 #VARIAVEL PARA DEFINIÇÃO DE STRING
fem = masc = 0 #VARIAVEIS PARA CONTAGEM
saida = 'S' #VARIAVEL QUE CONDICIONA A SAÍDA
while masc == 'M' or fem == 'F' or saida == 'S': #ENQUANTO SATISFAZER A CONDIÇÃO O PROGRAMA APRESENTA O LAÇO FOR [1,10]
    for s in range(1, 10):
        sexo = str(input('\033[2:32mDigite o sexo [M/F]:\033[m ')).upper() #INPUT PARA CONDIÇÃO
        if sexo == 'M' or sexo == 'F': #CADEIA DE CARACTERES AVALIANDO SE MASC OU FEM PARA CONTAGEM
            if sexo == 'M':
                masc += 1 #CONTADOR MASCULINO
            elif sexo == 'F':
                fem += 1 #CONTADOR FEMININO
        else: #CONDIÇÃO CASO AS LETRAS 'M E 'F' NÃO SEJA ATENDIDA
            print('\033[2:34mValor incorreto.\033[m')
    saida = str(input('\033[2:36mDeseja continuar [S/N]:\033[m ')).upper()
    #SAIDA É REFERENTE AO ENCERRAMENTO DO PROGRAMA. CASO O INPUT RECEBA O VALOR DA VARIAVEL FIXA O PROGRAMA SE ENCERRA
print('Foram verificados \033[2:32m{} homens\033[m e \033[2:33m{} mulheres\033[m'.format(masc, fem))
print('Fim!')'''

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor informe o sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
