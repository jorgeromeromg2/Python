from ex109 import moeda
preco = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}. ')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}. ')
print(f'Aumentando 10% de taxa temos {moeda.aumentar(preco, 10, True)}. ')
print(f'Diminuindo 13% de taxa temos {moeda.diminuir(preco, 13, True)}. ')
