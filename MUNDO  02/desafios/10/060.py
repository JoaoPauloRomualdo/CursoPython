""" Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120 """
n1 = int(input('Digite um numero para calcular seu fatorial: '))

c = n1
f = 1
print(f'Calculando {n1}! =', end=' ')
while c > 0:
    print(f'{c}', end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f *= c
    c -= 1

print(f'{f}')
