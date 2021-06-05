#--------CATEGORIA NATAÇÃO--------#
print(10 * '--=--')
print('CADASTRO PARA CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print(10 * '--=--')
nome = str(input('Qual é o seu nome: ')).capitalize()
idade = int(input('Qual é a sua idade: '))
if idade <= 9:
    print('{}, você tem {} anos e está cadastrado na categoria MIRIM.'.format(nome, idade))
elif idade <= 14:
    print('{}, você tem {} anos e está cadastrado na categoria INFANTIL.'.format(nome, idade))
elif idade <= 19:
    print('{}, você tem {} anos e está cadastrado na categoria JUNIOR.'.format(nome, idade))
elif idade <= 20:
    print('{}, você tem {} anos e está cadastrado na categoria SENIOR.'.format(nome, idade))
else:
    print('{}, você tem {} anos e está cadastrado na categoria MASTER.'.format(nome, idade))