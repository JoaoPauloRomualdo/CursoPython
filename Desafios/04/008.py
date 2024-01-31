""" Desafio 008

Desenvolva um programa que leia um valor em metros e o exiba
convertido em centimetros e milimetros . """

valor_metros = float(input('Digite o valor em metros para ser convertido : '))

valor_decimetro = valor_metros / 10

valor_centimetros = valor_metros * 100

valor_milimetros = valor_metros * 1000

valor_decametro = valor_metros * 10

valor_hectometro = valor_metros * 100

valor_quilometro = valor_metros * 1000

print(f'O valor em metros digitado foi {valor_metros},\nvalor em decimetro sera : {valor_decimetro},\nconvertido em centimetros sera {valor_centimetros},\n valor em milimetros sera {valor_milimetros}')

print(f'Seu valor convertido em decâmetro coresponde : {valor_decametro},\nseu valor em hectômetro corresponde : {valor_hectometro},\ne seu valor em quilômetros corresponde : {valor_quilometro}')