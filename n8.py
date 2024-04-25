def calcular_pessoas_da_festa():

    lista_de_convidados = []
    input_pessoa = int(input('digite a quantidade de pessoas: '))

    for convidados in range(input_pessoa):
        convidados += 1
        nomes = input('Informe o nome da pessoas : ' +
              str(convidados) + ' ')
        lista_de_convidados.append(nomes)


    for convidados in lista_de_convidados:
        print(convidados)

calcular_pessoas_da_festa()