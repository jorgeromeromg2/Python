#import
#ou
from OnzeAnos import numeros

num = int(input('Digite um número: '))
fat = numeros.fatorial(num)
print()
print(f'O fatorial de {num} é {fat}, o dobro é {numeros.dobro(num)} e o tríplo é {numeros.triplo(num)}')
