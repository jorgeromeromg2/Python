try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados que você digitou. ')

except ZeroDivisionError:
    print(f'Não foi possível dividir o número por zero! ')

except KeyboardInterrupt:
    print(f'O usuário preferiou não informar os dados! ')

except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')

else:
    print(f'O resultado é {r:.1f}')

finally:
    print('Volte Sempre! Muito Obrigado.')
