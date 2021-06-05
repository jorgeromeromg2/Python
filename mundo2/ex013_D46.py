#-------CONTAGEM REGRESSIVA------
from time import sleep
import emoji
print(10 * '-=')
print('\033[1:36mCONTAGEM REGRESSIVA\033[m')
print(10 * '-=')
inicio = int(input('Digite o primeiro número da contagem: '))
fim = int(input('Digite o último número da contagem: '))
for c in range(inicio, fim, -1):
    print(c)
    sleep(1)
print(emoji.emojize(':fireworks: :tada: \033[1:35mO tempo acabou!\033[m :tada: :fireworks:', use_aliases=True))

