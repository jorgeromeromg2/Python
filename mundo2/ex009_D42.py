#------VERIFICAR QUAL TIPO DE TRIANGULO-------
reta1 = float(input('Digite a primeira reta: ')) #cateto adjacente
reta2 = float(input('Digite a segunda reta: ')) #cateto oposto
reta3 = float(input('Digite a terceira reta: ')) #hipotenusa
if (reta1 + reta2 > reta3) and (reta2 + reta3 > reta1) and (reta1 + reta3 > reta2):
    print('Possui condição para ser um triângulo.')
    if reta1 != reta2 != reta3 != reta1:
        print('Este triângulo é escaleno.')
    elif reta1 == reta2 != reta3 or reta1 == reta3 != reta2 or reta2 == reta3 != reta1:
        print('Este triângulo é isósceles.')
    else:
        print('Este triângulo é equilátero.')
else:
    print('Não possui condição para ser um triângulo.')
