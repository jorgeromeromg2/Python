def voto(b):
    from datetime import datetime
    atual = datetime.now().year
    a = atual - b
    if a >= 18:
        return f'Com {a} anos: VOTO OBRIGATÓRIO.'
    elif 16 <= a < 18 or a >= 65:
        return f'Com {a} anos: VOTO OPCIONAL.'
    else:
        return f'Com {a} anos: NÃO VOTA.'


# Programa Principal
print('===' * 10)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
