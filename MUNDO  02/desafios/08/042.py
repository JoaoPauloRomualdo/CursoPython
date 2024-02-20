""" Exercício Python 042: 
    Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
    - EQUILÁTERO: todos os lados iguais
    - ISÓSCELES: dois lados iguais, um diferente
    - ESCALENO: todos os lados diferentes
 """
first_line = float(input('Digite o valor da primeira reta : '))
second_line = float(input('Digite o valor da segunda reta : '))
third_line = float(input('Digite o valor da terceira reta : '))

if first_line < second_line + third_line and second_line < first_line + third_line and third_line < first_line + second_line :
    print('As restas acima PODEM FORMAR UM TRIANGULO')

else :
    print('As retas acima NÃO PODEM FORMAR UM TRIANGULO')