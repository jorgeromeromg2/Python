'''def soma(a, b):
    s = a + b
    print(f"A soma de {a} e {b} é {s}")


# Programa Principal
soma(a=2, b=6)
soma(5, 7)
soma(6, 4)'''

'''def contador(*num):
    for c in num:
        print(c, end=' ')
    print('Fim')
    tam = len(num)
    print(f'Recebi os valores {num} e contém {tam} números')


contador(2, 4, 6, 8, 9)
contador(1, 3, 5, 7)
contador(0, 8)'''

'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    #print(lst)


# Programa Principal
valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)'''


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos a {s}')


soma(2, 5)
soma(9, 4, 3)
soma(1, 1, 5)
