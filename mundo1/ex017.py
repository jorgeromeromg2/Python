#----- CATETOS -----
#----- PRIMEIRO MODO ------

'''oposto = float(input('Comprimento do cateto oposto: '))
adjac = float(input('Comprimento do cateto adjacente: '))
hipo = (oposto ** 2 + adjac ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}.'.format(hipo))

#----- SEGUNDO MODO ----

import math
oposto = float(input('Comprimento do cateto oposto: '))
adjac = float(input('Comprimento do cateto adjacente: '))
hipo = math.hypot(oposto, adjac)
print('A hipotenusa vai medir {:.2f}.'.format(hipo))'''

#------- TERCEIRO MODO ------

from math import hypot
op = float(input('Comprimento do cateto oposto: '))
ad = float(input('Comprimento do cateto adjacente: '))
#hipo = hypot(op, ad)
#print('A hipotenusa vai medir {:.2f}.'.format(hypo))
print('A hipotenisa vai medir {:.2f}.'.format(hypot(op, ad)))

