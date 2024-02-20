""" 
Desafio 035
" a soma de dois lados é sempre menor que o terceiro lado."

Desenvolva um programa que leia o comprimentro de tres retas e diga ao usúario se elas podem ou não fomar um triangulo  """

first_line = float(input('Digite o valor da primeira reta : '))
second_line = float(input('Digite o valor da segunda reta : '))
third_line = float(input('Digite o valor da terceira reta : '))

if first_line < second_line + third_line and second_line < first_line + third_line and third_line < first_line + second_line :
    print('As restas acima PODEM FORMAR UM TRIANGULO')

else :
    print('As retas acima NÃO PODEM FORMAR UM TRIANGULO')