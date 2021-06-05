#-----CALCULAR O ANGULO ----
'''import math
angulo = float(input('Digite o ângulo que você deseja: '))
s = math.sin(math.radians(angulo))
c = math.cos(math.radians(angulo))
t = math.tan(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}.'.format(angulo, s))
print('O ângulo de {} tem o COSSENO de {:.2f}.'.format(angulo, c))
print('O ângulo de {} tem o TANGENTE de {:.2f}.'.format(angulo, t))'''

#------ IMPORTANDO APENAS OS MODULOS ----

from math import (sin, cos, tan, radians)
angulo = float(input('Digite o ângulo que você deseja: '))
s = sin(radians(angulo))
c = cos(radians(angulo))
t = tan(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}.'.format(angulo, s))
print('O ângulo de {} tem o COSSENO de {:.2f}.'.format(angulo, c))
print('O ângulo de {} tem o TANGENTE de {:.2f}.'.format(angulo, t))
