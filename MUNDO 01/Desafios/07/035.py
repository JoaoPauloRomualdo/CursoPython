""" 
Desafio 035
" a soma de dois lados é sempre menor que o terceiro lado."

Desenvolva um programa que leia o comprimentro de tres retas e diga ao usúario se elas podem ou não fomar um triangulo  """

first_line = float(input('Digite o valor da primeira reta : '))
second_line = float(input('Digite o valor da segunda reta : '))
third_line = float(input('Digite o valor da terceira reta : '))

triangle = first_line + second_line

if triangle <= third_line :
    print('OPA !!! As retas informadas conseguem formar um reta ')
else :
    print('Que pena as retas que você informou não e possivel formar um triangulo ')