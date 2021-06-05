#-----CALCULANDO O IMC------
nome = str(input('Qual é o seu nome: ')).capitalize()
sexo = str(input('Homem ou Mulher: '))
idade = int(input('Qual é a sua idade: '))
peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura ** 2)
if imc <= 16.9:
    print('\033[2:31m Cuidado {}, você está muito abaixo do peso. Seu IMC é {:.2f}.\033[m'.format(nome, imc))
    if sexo == 'homem':
        print('Pode apresentar queda de cabelo.')
    elif sexo == 'mulher':
        print('Pode apresentar queda de cabelo, ausência menstrual e infertilidade.')
elif imc <= 18.4:
    print('Seja cauteloso(a) {}, você está abaixo do peso.  Seu IMC é {:.2f}.'
          'Pode apresentar fadiga, stress e ansiedade.'.format(nome, imc))
elif imc <= 24.9:
    print('Parabéns {}, seu peso está normal. Seu IMC é {:.2f}. Continue cuidando da sua saúde.'.format(nome, imc))
elif imc <= 29.9:
    print('Seja cauteloso(a) {}, você está acima do peso. Seu IMC é {:.2f}.'.format(nome, imc))
elif imc >= 30:
    print('Cuidado, você entrou na obesidade!')
    if imc <= 34.9:
        print('Sua obesidade é considerada Grau I. Seu IMC é {:.2f}.Pode apresentar diabetes, angina, infarto e '
              'aterosclerose.'.format(imc))
    elif imc <= 40:
        print('Sua obesidade é considerada Grau II. Seu IMC é {:.2f}.Pode apresentar apneia do sono e falta de ar'
              .format(imc))
    elif imc > 40:
        print('Sua obesidade é considerada Grau III.  Seu IMC é {:.2f}.Pode apresentar refluxo, dificuldade para se'
              ' mover, escaras, diabetes, infarto, AVC'.format(imc))
