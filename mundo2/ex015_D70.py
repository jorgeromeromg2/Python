print('=='*20)
loja = 'LOJA TEM TUDO'
print(loja.center(40))
print('=='*20)
nome = str(input('Digite seu nome: ')).strip().upper()
produto = barato = ''
preco = contP = total = compra = precoAcima = menor = 0
while True:
    produto = str(input('Nome do produto: ')).strip()
    contP += 1
    preco = float(input('Preço: R$ '))
    compra += preco
    if preco > 1000:
        precoAcima += 1
    if contP == 1 or preco < menor:
        menor = preco
        barato = produto
    continuar = str(input('Deseja continuar [S]Sim ou [N]Não? ')).strip()[0]
    while continuar not in 'SsNn':
        continuar = str(input('\033[1:31mOpção inválida\033[m. Deseja continuar [S]Sim ou [N]Não? ')).strip()[0]
    if continuar not in 'Ss':
        break
print(f'{nome}, você comprou {contP} produtos que somados custaram R$ {compra:.2f} reais.')
print(f'{precoAcima} produto(s) custam mais de R$ 1.000,00 reais')
print(f'O produto mais barato é o(a) {barato} custando R$ {menor:.2f} reais.')
