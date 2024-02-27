""" Desafio 048
Faça um programa que calucle a soma entre todos os numeros impares que sao multiplos de tres e que se encontram no intervalo de 1 ate 500 """

soma = 0
cont = 0

for numero in range(1, 501, 2):  # Começa de 1, vai até 500, incrementando de 2 em 2 (ímpares)
    if numero % 3 == 0:  # Verifica se o número é múltiplo de três
        cont = cont + 1
        soma += numero   # Adiciona o número à soma

print(f"A soma de todos os {cont} múltiplos de três no intervalo de 1 a 500 é: {soma}")
