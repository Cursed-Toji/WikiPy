#Faça um Programa que peça dois números e imprima a soma.



def soma():
    try:
        numero1 = float(input('Informe o numero 1° '))
        numero2 = float(input('Informe o 2° numero '))
        resultado = numero1 + numero2
        print('O resultado foi de', resultado)
    except Exception as error:
        print(error)


def subtrair():
    try:
        numero1 = float(input('Informe o numero 1° '))
        numero2 = float(input('Informe o 2° numero '))
        resultado = numero1 - numero2
        return resultado
    except Exception as error:
        print(error)



def multiplicar():
    try:
        numero1 = float(input('Informe o numero 1° '))
        numero2 = float(input('Informe o 2° numero '))
        resultado = numero1 * numero2
        return resultado
    except Exception as error:
        print(error)




def dividir():
    try:
        numero1 = float(input('Informe o numero 1° '))
        numero2 = float(input('Informe o 2° numero '))
        resultado = numero1 / numero2
        return resultado
    except Exception as error:
        print(error)



def menu():
    print('escolha uma opção\n 1 somar\n 2 subtrair\n 3 multiplicar\n 4 dividir')



def carregar():
    while True:
        menu()
        opcao= input('Esclha a opção: ')

        if opcao == '1':
            soma()

        elif opcao == '2':
            soma()

        elif opcao == '3':
            soma()

        elif opcao == '14':
            soma()


carregar()