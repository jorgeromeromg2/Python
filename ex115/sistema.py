from Python.ex115.lib.interface import *
from Python.ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvídeo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Criar Arquivo', 'Cadastrar Pessoas', 'Listar Cadastros', 'Sair do Sistema'])
    if resposta == 1:
        linha()
        arq = str(input('Digite o nome do arquivo a ser criado: '))
        criarArquivo(arq)
    elif resposta == 2:
        linha()
        cabeçalho(f'NOVO CADASTRO')
        nome = str(input('Nome: ').capitalize())
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        linha()
        lerArquivo(arq)
    elif resposta == 4:
        linha()
        cabeçalho(f'\033[1;30;42mSaindo do Sistema... Até logo.\033[m')
        break
    else:
        linha()
        cabeçalho('Erro! Digite uma opção válida.')
    sleep(2)
