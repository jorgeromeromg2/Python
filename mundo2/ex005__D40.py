#-------MÉDIA FINAL-----
from time import sleep
aluno = str(input('Nome do aluno: ')).capitalize()
nota1 = float(input('Digite a nota do primeiro semestre: '))
nota2 = float(input('Digite a nota do segundo semestre: '))
nota3 = float(input('Digite a nota do terceiro semestre: '))
print('CALCULANDO...')
sleep(3)
media = (nota1 + nota2 + nota3)/3
if media < 5:
    print('\033[1:31m {}, sua média foi {:.2f} infelizmente você não atingiu a média.\033[m'
          ' \033[2:31:107m REPROVADO! \033[m'.format(aluno, media))
elif (media >= 5) and (media <= 6.9):
    print('\033[2:34m{}, sua média foi {:.2f}. Você está de\033[m \033[2:33m RECUPERAÇÃO!\033[m'.format(aluno, media))
else:
    print('\033[2:32m Parabéns {}, sua média foi {:.2f}. Você está\033[m \033[2:92:41m '
          'APROVADO!\033[m'.format(aluno, media))
