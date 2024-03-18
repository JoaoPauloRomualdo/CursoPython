""" Desafio 74 

Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla, Depois disso mostre a listagem dos numeros gerados e também indique o menor e o maoior valor que estão na tupla """

from random import randint


lista_numero =(randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(lista_numero)
print(f' O maior numero gerado na lista foi {max(lista_numero)}')
print(f'O menor numero gerado na lista foi {min(lista_numero)}')