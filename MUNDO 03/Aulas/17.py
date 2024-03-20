num = [ 2, 5 , 9 , 1 ]

num[2] = 3 #Altero o valor de 2 para 3

num.append(7) #Adiciono o valor 7 a lista 

num.sort()#Vai ordenar nossa lista de forma crescente

num.sort(reverse=True)#Vai ordenar a lista de forma reversa

num.insert(2,2)#Vou adicionar o zero na posição dois

#num.pop()#Ele remove o ultimo elemento da lista se nao passarmos nenhum parametro para ele

#num.pop(2)#Ira remover o elemento que esta na posição dois

if 4 in num :
    num.remove(4)#Ira remover o primeiro valor dois que e encontrado na lista
else:
    print('Valor nao encontrado')

print(num)

print(f'Essa lista tem {len(num)} elementos')#Metodo len sabemos quantos elementos possui dentro da lista

valores = []


# P A R A - M O S T R A R - U M A - L I S T A - O R G A N I Z A D A
""" valores.append(5)
valores.append(9)
valores.append(4)

print(valores)
#para mostrar um lista mais organizada
for v in valores:
    print(f'{v}...',end=' ')

for c, v in enumerate(valores):
    print(f'\nNa posicao {c} encotrei o valor {v}')

print('Cheguei no final da lista') """

# P A R A - I N S E R I R - V A L O R E S - A T R A V E S - D O - T E C L A D O 
""" 
for cont in range(0, 5):
    valores.append(int(input('Digite um valor : ')))

for c, v in enumerate(valores):
    print(f'Na posicao {c} encotrei o valor {v}')

print('Cheguei no final da lista') """

a = [ 2, 3, 4, 7]
b = a[:]
b[2]= 8

print(f'lista A: {a}')
print(f'lista B: {b}')