""" Desafio 008

Desenvolva um programa que leia um valor em metros e o exiba
convertido em centimetros e milimetros . """

valor_metros = float(input('Digite o valor em metros para ser convertido : '))

valor_centimetros = valor_metros * 100

valor_milimetros = valor_metros * 1000

print(f'O valor em metros digitado foi {valor_metros},convertido em centimetros sera {valor_centimetros}, valor em milimetros sera {valor_milimetros}')