def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas de alunos (aceita várias)
    :param sit: valor opcional, indicando se deev ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    r = {}
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["média"] = sum(n)/len(n)
    if sit:
        if r["média"] >= 7:
            r["situação"] = 'BOA'
        elif r["média"] >= 5:
            r["situação"] = 'RAZOÁVEL'
        else:
            r["situação"] = 'RUIM'
    return r


#Programa Principal
n1 = float(input(f'Digite a nota: '))
n2 = float(input(f'Digite a nota: '))
n3 = float(input(f'Digite a nota: '))
n4 = float(input(f'Digite a nota: '))
resp = notas(n1, n2, n3, n4, sit=False)
print(resp)
help(notas)
