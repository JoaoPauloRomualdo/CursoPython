""" Desafio 030

Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar """

print('='* 80)
print('DIGITE UM NÚMERO E VAMOS VERIFICAR SE ELE E IMPAR OU PAR !!!')
print('='* 80)

number = int(input('Digite um numero: '))

check = number % 2

if check == 0 :
    print(f'Número digitado foi {number}, este número e PAR !!!')
else:
    print(f'O número digitado foi {number}, este número e IMPAR')