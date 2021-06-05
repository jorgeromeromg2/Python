'''teste = list()
teste.append('Jorge')
teste.append('32')
galera = []
galera.append(teste[:])
teste[0] = 'Maíra'
teste[1] = 28
galera.append(teste)
print(galera)'''

'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for g in galera:
    print(f'{g[0]} tem {g[1]} anos.')'''

galera = []
dados = []
mai = men = 0
contF = contM = 0
while True:
#for d in range(0, 5):
    dados.append(str(input('Digite o nome: ').capitalize()))
    dados.append(int(input('Digite a idade: ')))
    dados.append(str(input('Digite o sexo [M/F]: ')))
    galera.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar?'))
    if continuar in 'Nn':
        break
for g in galera:
    if g[1] >= 18:
        print(f'{g[0]} é maior de idade.')
        mai += 1
        if g[2] in 'Mm':
            contM += 1
        else:
            contF += 1
    else:
        print(f'{g[0]} é menor de idade.')
        men += 1
        if g[2] in 'Mm':
            contM += 1
        else:
            contF += 1
print(f'{mai} pessoas são maiores e {men} pessoas são menores.')
print(f'{contM} homens e {contF} mulheres')