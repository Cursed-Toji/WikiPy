

# while convidados <= numero_de_convidados:
#     nome_do_convidado = input('digite o nome: ' + str(convidados) + ' ')
#     convidados += 1
print('programa de controle de festas')
print('---------------------------------------')

numero_de_convidados = int(input('digite a quantidade de convidados: '))

# Foi criado essa lista para puxar os nomes dos convidados
lista_de_convidados = []
convidados = 1

for convidado in range(numero_de_convidados):
    nome_do_convidado = input('digite o nome: ' + str(convidados) + ' ')
    convidados += 1
    #toda vez que fo
    lista_de_convidados.append(nome_do_convidado)


for convidado in (lista_de_convidados):
    print(convidados)


