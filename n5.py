#Faça um Programa que converta metros para centímetros.
def metros_para_centimetros():
     metros = float(input('digite o valor em metros:'))
     resultado = metros * 100
     print('-----------------')
     print('####',resultado, '####')
     print('-----------------')

def menu():
    print('este programa calcula a quantidade de metro para centimetros')


def carregar():
    menu()
    while True:
        try:
          opcao = int(input('informe 1 para calcular\ninforme 2 para sair\nopção: '))
          if opcao == 1:
              metros_para_centimetros()
          elif opcao == 2:
                break
          else:
              print('informe apenas numeros')

        except Exception as error:
            print('error noooo', error)

carregar()