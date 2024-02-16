""" 
Desafio 010
Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira
e mostre quantos Dolares ela pode comprar . """

dinheiro = float(input('Ola quantos reais você deseja converter:'))

dolar = 4.92

conversao = dinheiro / dolar

print(f'Você possui R$: {dinheiro:.2f}, seu novo valor em dolares sera U$: {conversao:.2f}')