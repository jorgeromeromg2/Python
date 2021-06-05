#-----ALISTAMENTO MILITAR------
from datetime import date
idade = int(input('Digite o ano de nascimento e descubra se está no ano para alistamento: '))
ano = date.today().year - idade
if ano < 17:
    print('\033[2:33m Você ainda precisa aguardar {} anos para se alistar. \033[m'.format(18-ano))
elif (ano >= 18) and (ano <= 21):
    print('\033[2:34m Você deve se alistar neste ano! \033[m')
else:
    print('\033[2:35m Seu tempo de alistamento já passou \033[m')
