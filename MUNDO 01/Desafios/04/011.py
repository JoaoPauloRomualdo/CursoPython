""" Desafio 011
Faça um programa que leia a largura de uma parede em metros. Cacule sua area e a 
quantidade de tinta necessaria para pinta-la ,
sabendo que cada litro de tinta pinta uma area de 2m²
"""

largura = float(input('Agora digite a largura de sua parede')) 

altura = float(input('Digite a altura de sua parede'))


qtd_tinta = (altura * largura) / 2

print(f'Sua altura da parede e : {altura}, e sua largura é : {largura}, quantidade de tinta a ser utilizada será : {qtd_tinta} litros de tinta')