#-------MEDIA DAS NOTAS
#n1 = float(input('Digite a primeira nota: '))
#n2 = float(input('Digite a segunda nota: '))
#media = (n1 + n2)/2
#print('A média das notas é: {}'.format(media))


#-----CONVERSOR DE METROS
#m1 = int(input('Digite uma distancia em metros: '))
#print('A distância digitada em centímetro é: {}cm'.format(m1*100))
#print('A distância digitada em milímetros é: {}mm'.format(m1*1000))

#------CONVERSAO PARA DOLARES
#valor1 = float(input('Quantos reais você tem na carteira: R$'))
#valor2 = float(valor1 / 5.65)
#if (valor2 >= 5.65):
#    print('Você pode comprar {:2f} dólar.'.format(valor2))
#else:
#    print('Você pode comprar {:2f} dólares.'.format(valor2))

#-------LITROS POR METROS QUADRADOS-------
#altura = float(input('Qual a altura da parede: '))
#largura = float(input('Qual a largura da parede: '))
#metros = (altura * largura)/2
#print('A parede tem {} de altura e {} de largura. São necessários {} litros de tinta'.format(altura, largura, metros))

#-------DESCONTO-------
#preco1 = float(input('Digite o preço do produto: '))
#preco2 = int(input('Quanto foi o desconto: '))
#desconto = preco1 - ((preco1 * preco2)/100)
#print('Você vai pagar R$ {} reais pelo produto.'.format(desconto))

#-------AUMENTO DE SALARIO-------
#salario1 = float(input('Digite seu salário atual: R$'))
#salario2 = int(input('Quantos porcentos foi prometido: '))
#aumento = ((salario2 * salario1)/100) + salario1
#print('Seu salário atual será de R$ {} reais'.format(aumento))

#------DESCUBRA QUANDO VOCE NASCEU-----
#idade = int(input('Quantos anos você faz em 2021: '))
#nome = str(input('Qual é o seu nome: '))
#ano = int(2021 - idade)
#print('{}, você nasceu no ano de {}.'.format(nome, ano))

#-------QUEM É VOCÊ?------
#idade = int(input('Digite a idade atual de um membro da família: '))
#if (idade == 7):
#    print('Olá Gustavo, você faz parte da família.')
#elif(idade == 10):
#    print('Olá Geovanna, você faz parte da família.')
#elif(idade == 27):
#    print('Olá Maíra, você faz parte da família.')
#elif(idade == 32):
#    print('Olá Jorge, você faz parte da família.')
#elif(idade != [8, 10, 27, 33]):
#    print('Não há ninguém nessa família com {} anos.'.format(idade))

#----------TABUADA------------
#num = int(input('Digite um número: '))
#print('-'*20)
#print('{} x {:2} = {}'.format(num, 1, num*1))
#print('{} x {:2} = {}'.format(num, 2, num*2))
#print('{} x {:2} = {}'.format(num, 3, num*3))
#print('{} x {:2} = {}'.format(num, 4, num*4))
#print('{} x {:2} = {}'.format(num, 5, num*5))
#print('{} x {:2} = {}'.format(num, 6, num*6))
#print('{} x {:2} = {}'.format(num, 7, num*7))
#print('{} x {:2} = {}'.format(num, 8, num*8))
#print('{} x {:2} = {}'.format(num, 9, num*9))
#print('{} x {:2} = {}'.format(num, 10, num*10))
#print('-'*20)

dias = int(input('Quantos dias com o auto: '))
distancia = float(input('Quantos Km rodados: '))
tempo = (dias * 60) + (distancia * 0.15)
print('O valor a pagar é R$ {:.2f}'.format(tempo))