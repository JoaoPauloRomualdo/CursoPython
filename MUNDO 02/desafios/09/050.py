""" Desafio 050
Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares se o valor digitado for impar desconsidere-o"""


soma = 0
cont = 0
for i in range(6):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    if numero % 2 == 0:
        soma += numero
        cont = cont +1

print(f"Você informou {cont} pares ,a soma dos números digitados é: {soma}")

