numero_de_convidados = input ("Coloque o numero de convidados")
lista_de_convidados= []

i = 1
while i <= int(numero_de_convidados):
    nome_do_convidado = input("Escreva o nome do convidado #" + str(i)+":")
    lista_de_convidados.append(nome_do_convidado)
    i += 1

print(lista_de_convidados)

for convidado in lista_de_convidados:
    print(convidado)

