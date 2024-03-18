""" 055
Faça um programa que leia o peso de cinco pessoas .No final mostre qual foi o maior e o menor pesso lidos. """


biggest_weight = []

for i in range(1,6):
    weight = float(input(f'Por favor , informe seu peso em  da {i}° pessoa(KG) : '))
    biggest_weight.append(weight)

print(f'maoir pesso informado foi {max(biggest_weight)} e o menor peso informado foi {min(biggest_weight)}')
