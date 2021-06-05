from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
sexo = str(input('Digite seu sexo: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if sexo == 'masculino':
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento.'.format(saldo))
        alista = atual + saldo
        print('Seu alistamento será em {}'.format(alista))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        alista = atual - saldo
        print('Seu alistamento foi em {}'.format(alista))
elif sexo == 'feminino':
    print('Mulher não possui alistamento obrigatório. O ingresso é por meio de concurso.')
else:
    print('Sexo inválido')
