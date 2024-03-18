#------------ TULAS SÃO IMUTÁVEIS !!!!

lanche = ('hamburguer','Suco','Pizza','Pudim','Batata Frita')
print(lanche)
#Mostra qual valor esta no index [1] dentro da varivael lanche
print(lanche[1])
print(lanche[3])

print(lanche[-2])
print(lanche[1:3])#Mostra os valores do elemento [1] ate o [3] so que o terceiro elemento e ignorado na hora que realiza o fatiamento

print(lanche[2:])#Mostra os valores do elemento [2] ate o final
print(lanche[:2])#Mostra os valores do inicio ate o elemento [2] ignorando o elemento dois

""" for c in lanche:#Maneira classica se nao precisar de posição
    print(f'Eu vou comer {c}')
print('Comi demias !!!')

for cont in range(0, len(lanche)):#Se precisar de posição
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi demias !!!')

for pos, i in enumerate(lanche):
    print(f'Eu vou comer {i} na posição {pos}')
print('Comi demias !!!') """
print(sorted(lanche))

a = (2,5,4)
b = (5,8,1,2)

c = b + a #Nao vai somar os valores dentro da tuplas mas sim vai juntar dentro da variavel c
print(c)
print(c.count(5))#Ira mostrar quantas vezes aparece o numero 5
print(c.index(8))#Mostra qual posição esta o numero 8 dentro da tupla

pessoa = ('Joao', 29, 'M', 99.88)
del(pessoa)
print(pessoa)