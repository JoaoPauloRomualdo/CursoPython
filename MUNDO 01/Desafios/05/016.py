""" Desafio 016 

Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

Ex: Digite um número : 6.127
    o número 6.127 tem a parte inteira 6 """

from math import trucn
number = float(input('Digite um número real : '))

print(f'A porção inteira de {number} sera {trucn(number)}')