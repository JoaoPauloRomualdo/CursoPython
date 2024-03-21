""" Desafio 078

Faça um programa que leia 5 valores numericos e guarde-os em uma lista, no final mostre qual foi o maior e o menor valor digitado e as respectivas posições na lista """
cont = 0
numeros = []

while cont <= 4:
    cont += 1
    num = numeros.append(int(input(f'Digite o {cont}° número : ')))

posicao_maior = 0
posicao_menor = 0

for i, valor in enumerate(numeros):
    if valor > numeros[posicao_maior]:
        posicao_maior = i
    elif valor < numeros[posicao_menor]:
        posicao_menor = i

print(f'O maior numero digitado foi {max(numeros)} e se encontra na {posicao_maior+1}° posição')
print(f'O menor número digitado foi {min(numeros)} e se econtra na {posicao_menor+1}° posição ')
print(numeros)
