times = ('Flamengo', 'Internacional', ' Atlético - MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos',
         'Atlético - PR', 'Bragantino', 'Ceará', 'Corintians', 'Atlético - GO', 'Bahia', 'Sport', 'Fortaleza', 'Vasco',
         'Goias', 'Coritiba', 'Botafogo')
br = 'CLASSIFICAÇÃO BRASILEIRO 2020/2021'
print('=='*30)
print(br.center(60))
print('=='*30)
print(f'Lista de Times do Brasileirão: {times}')#TIMES DO BRASILEIRO
print('=='*30)
print(f'Os cinco primeiros colocados são: {times[0:5]}')#OS CINCO PRIMERIOS COLOCADOS
print('=='*30)
print(f'Os quatro últimos colocados são: {times[-4:]}')#OS QUATRO ULTIMOS DA TABELA
print('=='*30)
print('Times em ordem alfabética:')
print(sorted(times))#TABELA EM ORDEM ALFABÉTICA
print('=='*30)
print(f'O Bragantino é o {times.index("Bragantino")+1}º colocado.')#EM QUE POSIÇÃO FICOU O TIME DO BRAGANTINO
print('=='*30)
