numero_de_convidados=input("Quantas pessoas serao convidadas")
lista_de_convidados=[]

i = 1
while i <= int(numero_de_convidados):
    Nome_dos_convidados= input("Escreva o nome do convidado #" + str(i) + ":")
    lista_de_convidados.append(Nome_dos_convidados)
    i += 1

print(lista_de_convidados)

for convidado in lista_de_convidados:
    print(convidado)

