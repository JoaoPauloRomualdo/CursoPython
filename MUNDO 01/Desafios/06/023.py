""" Desafio 023
Faça um programa que leia número de 0 a 9999 e mostre na tela cada um dos digitos separados

Ex : Digite um número: 1834

unidade: 4
dezena : 3
centena : 8
milhar : 1 """

number = int(input('Digite um numero inteiro qualquer : '))
unidade = number // 1 % 10
dezena = number // 10 % 10
centena = number // 100 % 10
milhar = number // 1000 % 10
print(f'Analisando o número: {number}')
print(f'Unidade :{unidade}')
print(f'Dezena : {dezena}')
print(f'Centena : {centena}')
print(f'Milhar : {milhar}')

print(number.split())