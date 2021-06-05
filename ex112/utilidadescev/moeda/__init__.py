def metade(preço=0, formato=False):
    """
    -> Função que retorna a metade de um determinado preço informado em 'teste'.
    :param preço:  variável recebida de teste para ser verificada na função metade.
    :param formato: verifica a condição para a variável res ser formatada com a função 'moeda'.
    :return: retorna o calculo da função
    """
    res = preço/2
    return res if not formato else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$ '):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço=0, taxa1=0, taxa2=0):
    print('---' * 10)
    print(f'RESUMO DO VALOR'.center(30))
    print('---' * 10)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'O dobro do preço: \t{dobro(preço, True)}')
    print(f'A metade do preço: \t{metade(preço, True)}')
    print(f'{taxa1}% de aumento: \t{aumentar(preço, taxa1, True)}')
    print(f'{taxa2}% de diminuição: \t{diminuir(preço, taxa2, True)}')
    print('---' * 10)
