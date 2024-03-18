""" Desafio 047
Crie um programa que mostre na tela tods os números pares que estão no intervalo entre 1 a 50
 """

for i in range(2,50,2):
    n = i % 2
    if n == 0 :
        print(f'Os numeros pares de 1 a 50 sao {i}')
