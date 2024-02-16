""" Desafio 017

Faça um programa que leia o comprimento de um cateto oposto e do cateto adjacente de um triângulo retangulo , calcule e mostre o comprimento da hipotenusa  """

from math import hypot

cateto = float(input('Digite o valor do cateto oposto : '))

cateto_adjacente = float(input('Digite o valor do cateto adjacente : '))


hipotenusa = hypot(cateto, cateto_adjacente)

print(f'A hipotenusa vai medir {hipotenusa:.2f}')
