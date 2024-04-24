print('programa feito para ver quantas pessoas vão para a festa da empresa\n')

try:
    numero_de_pessoas = int(input('quantas pessoas vão participar: '))
except ValueError:
    print('digite um numero inteiro')
except Exception as Erros:
    print(Erros)
#aqui vai ficar vazio pra poder puxar
lista_de_pessoas = []

for pessoas in range(numero_de_pessoas):
    pessoas = 1
    input_pessoa = input('digite o nome do funcionario: ' + str(pessoas) + " ")
    print('---------------------------------')

    pessoas += 1
    #o apeend e pra poder adicionar as pessoas
    lista_de_pessoas.append(input_pessoa)

print(lista_de_pessoas)


def calcular_pessoas_da_festa():
    convites = 1
    lista_de_convidados = []
    input_pessoa = input('digite a quantidade de pessoas')

    for convidados in range(input_pessoa):
        convidados = +1
        nomes = input('Informe o nome da pessoas : ' + 'Numero da pessoas na listagem' +
              str(convidados) + '')
        lista_de_convidados.append(nomes)

    for convidados in lista_de_convidados:
        print(convidados)




