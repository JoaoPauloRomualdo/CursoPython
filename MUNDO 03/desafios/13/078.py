""" Desafio 078

Faça um programa que leia 5 valores numericos e guarde-os em uma lista, no final mostre qual foi o maior e o menor valor digitado e as respectivas posições na lista """
numeros = []
cont = 0
posicao_maior = 0
posicao_menor = 0

for c in range(0,5):
    cont += 1
    numeros.append(int(input(f'Digite um valor para posição {c} : ')))

    if c == 0 :
        posicao_maior = posicao_menor = numeros[c]
    else:
        if numeros[c] > posicao_maior:
            posicao_maior = numeros[c]
        if numeros[c] < posicao_menor:
            posicao_menor = numeros[c]

print(f'Os valores digitado foram {numeros}')
print(f'O maior numero digitado foi {posicao_maior} nas posições : ',end=' ')
for i , v in enumerate(numeros):
    if v == posicao_maior:
        print(f'{i}...',end= ' ')
print()

print(f'O menor numero digitado foi {posicao_menor} nas posições :',end=' ')

for i, v in enumerate(numeros):
    if v == posicao_menor:
        print(f'{i}...',end= ' ')
print()   