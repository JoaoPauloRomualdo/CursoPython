""" Desafio 015
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado. """
quantidade_dia = int(input('Digite a quantidade de dias que você utilizou o veiculo : '))

quantidade_km = float(input('Digite a quantidade de KM : '))


valor = quantidade_km * 0.15 + quantidade_dia * 60

print(f'Você utilizou o carro {quantidade_dia} dias e rodou {quantidade_km} KM , total a sera pago sera :{valor}')