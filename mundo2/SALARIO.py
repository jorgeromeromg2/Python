def horas(h1, tota):
    salario = h1 * tota
    ir = salario * 0.11
    inss = salario * 0.08
    sindicato = salario * 0.05
    soma = ir + inss + sindicato
    total = salario - soma
    hora_liquida = total/220
    print(f'salario bruto: R$ {salario:.2f}\ndesconto ir: R$ {ir:.2f} \ninss: R$ {inss:.2f} '
          f'\nsindicato: R$ {sindicato:.2f} \nsalario liquido: R$ {total:.2f} \nhora liquida: R$ {hora_liquida:.2f}')


try:
    h1 = int(input("Digite o valor bruto da sua hora trabalhada: "))
    h2 = int(input("Digite a quantidade de horas mes trabalhada: "))
    horas(h1, h2)

except:
    print('ops:só e valido números! tente novamente!')


'''def horas(h1, h2, nome):
    empregado = nome
    salario = h1 * h2
    ir = salario * 0.11
    inss = salario * 0.08
    sindicato = salario * 0.05
    soma = ir + inss + sindicato
    total = salario - soma
    hora_liquida = total / 220
    salario = {
        "Nome :": empregado,
        "salario bruto : R$ ": salario,
        "Imposto de renda : R$ ": ir,
        "inss : R$ ": inss,
        "Sindicato : R$ ": sindicato,
        "Salario liquido : R$ ": total,
        "Horas liquidas : R$ ": hora_liquida,
    }
    for k, v in salario.items():
        print(f'{k}:{v}')


try:
    nome = input("Digite seu nome: ").capitalize()
    h1 = float(input("Digite o valor bruto da sua hora trabalhada: "))
    h2 = float(input("Digite a quantidade de horas mes trabalhada: "))
    horas(h1, h2, nome)
    
    
except:
    print('ops:só e valido números! tente novamente!')'''