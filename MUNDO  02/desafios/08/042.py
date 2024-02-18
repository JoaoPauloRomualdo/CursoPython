""" Exercício Python 042: 
    Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
    - EQUILÁTERO: todos os lados iguais
    - ISÓSCELES: dois lados iguais, um diferente
    - ESCALENO: todos os lados diferentes
 """
first_line = float(input('Digite o valor da primeira reta : '))
second_line = float(input('Digite o valor da segunda reta : '))
third_line = float(input('Digite o valor da terceira reta : '))

triangle = first_line + second_line

if triangle <= third_line :
    print('OPA !!! As retas informadas conseguem formar um reta ')
    if first_line == second_line and first_line == third_line:
        print(f'O tringulo que sera formado sera um triangulo EQUILÁTERO, onde todos os lados são iguais')
    elif first_line != second_line and second_line == third_line :
        print(f'O tringulo que sera formado sera um trigunlo ISÓSCELES , onde dois lados são iguais e um lado e diferente')
    elif first_line != second_line and first_line != third_line :
        print(f'O trngulo que sera formado e um triangulo ESCALENO, onde são todos os lados diferentes')
else :
    print('Que pena as retas que você informou não e possivel formar um triangulo  ')