""" Desafio 012 
Faça um algoritmo que leia a preço de um produto e mostre seu novo preço
com 5% de desconto
"""

preco_produto = float(input('Digite o valor do produto que ira receber o desconto'))

desconto = preco_produto * 0.05

novo_valor = preco_produto - desconto

print(f'Valor do produto original e {preco_produto}, valor do desconto aplicado será : {desconto}, valor do produto com desconto será : {novo_valor}')