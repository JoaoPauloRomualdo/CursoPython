""" teste = list ()
teste.append('Joao')
teste.append(29)
galera = list()
galera.append(teste[:])#Ultilizamos para fazer copia nas listas
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(teste)
print(galera) """

########################################################
""" galera = [['Joao', 19], ['Ana', 33], ['Joaquim', ' 13'], ['Maria', 45]]

print(f'* {galera}')
print(f'* {galera[0]}')
print(f'* {galera[0][0]}')

for p in galera :
    #print(p)#Ira mostrar a lista ordenada com todos os valores
    #print(f'-> {p[0]}')#Ira mostrar somentes o nomes das pessoas 
    #print(f'-> {p[1]}')#Ira mostrar somentes o idade das pessoas 
    print(f'{p[0]} possue {p[1]}, anos de idade')# print formatado com a idade e o nome das pesssoas  """

galera = list()
dado = list()
totmaior = totmenor = 0
for c in range(0,3):
    dado.append(str(input('Digite seu nome : ')))
    dado.append(int(input('Digite sua idade : ')))
    galera.append(dado[:])
    dado.clear()

for p in galera: 
    if p[1] >= 21: #Ira mostrar somente as pessoas que possuem mais de 21 anos
        print(f'{p[0]} e maior de idade ')
        totmaior += 1
    else:
        print(f'{p[0]} e menor de idade ')
        totmenor += 1

print(f'Temos {totmaior} pessoas maiores e {totmenor} menores de idade')