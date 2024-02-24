""" Desafio 049
Refaça o Desafio 009 , mostrando a tabuado de um número que o usuario escolher . so que a gora utilizando um laço for """

print('Ola, digite qualquer número e vamos mostrar a tabuada dele')

number = int(input('Digite um número : '))

for i in range(1,11):
    tabuada = number * i
    print(f'{number} X {i} = {tabuada}')

print('Sua tabuada esta pronta !!!')