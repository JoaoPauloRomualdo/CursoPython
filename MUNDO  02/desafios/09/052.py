""" 052
Faça um programa que leia um numero inteiro e diga se ele e ou nao um numero primo """

num = int(input('Digite um numero: '))
tot = 0
for i in range (1,num +1):
    if num % i == 0:
        tot += 1

print(f'O numero {num} foi divisivel {tot} vezes')

if tot ==2 :
    print('E por isso ele é primo')

else :
    print('E por isso ele não e primo')