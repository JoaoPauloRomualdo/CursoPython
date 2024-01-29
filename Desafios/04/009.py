""" Desafio 009 
Faça um programa que leia um numero inteiro e mostre na tela a sua tabuada. """
print('Ola digite um número e vamos fazer uma tabuada para você')

numero = int(input('Digite um número: '))

print(f'A tabuado do {numero}')

for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} * {i} = {resultado} ')