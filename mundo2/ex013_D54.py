#-------MAIORIDADE-------
from datetime import date
cont1 = 0
cont2 = 0
for i in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i)))
    if date.today().year - ano >= 21:
        cont1 += 1
    else:
        cont2 += 1
print('{} datas atingiram a maioridade'.format(cont1))
print('{} datas NÃO atingiram a maioridade'.format(cont2))