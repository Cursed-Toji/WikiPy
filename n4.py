#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def calcular_media_do_aluno():
    nota1 = float(input('informe a nota do aluno'))
    nota2 = float(input('informe a nota '))
    nota3 = float(input('informe a nota'))
    nota4 = float(input('informe a nota'))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print()
    print('a media do aluno é de: ', media)
    print()


def menu():
    print('Para calcular a nota do Aluno informe 1\n para sair do sistema informe 2')



def carregar():

    while True:
        menu()
        informe = int(input('Sessão desejada'))
        if informe == 1:
            calcular_media_do_aluno()
        elif informe == 2:
            print('Saiu do sistema')
            break


carregar()