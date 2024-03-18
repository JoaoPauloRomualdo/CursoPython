""" Desafio 051
Desenvolva um programa que leia o primeiro termo e a razao de uma PA.no final mostre 10 primeiros termos dessa progressão """

primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

print("Os 10 primeiros termos da PA são:")

for i in range(10):
    termo = primeiro_termo + i * razao
    print(termo, end=" ")

# Caso queira imprimir os termos em linhas separadas, remova o end=" " do print acima.
