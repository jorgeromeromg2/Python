from datetime import datetime
relacao = dict()
relacao["Nome"] = str(input('Nome: ')).capitalize()
idade = int(input('Ano de nascimento: '))
relacao["Idade"] = datetime.now().year - idade
relacao["CTPS"] = int(input('Carteira de Trabalho (0 não tem): '))
if relacao["CTPS"] != 0:
    relacao["Contratação"] = int(input('Ano de Contratação: '))
    relacao["Salário"] = float(input('Salário: '))
    relacao["Aposentadora"] = relacao["Idade"] + ((relacao["Contratação"] + 35) - datetime.now().year)
for k, v in relacao.items():
    print(f'{"-":>5} {k} tem o valor {v}')

