""" Desafio 057
Faça um programa que leia o sexo de uma pessoa, mas so aceite os valores 'M' ou 'F'.Caso esteja errado , peça a digitação novamente ate ter um valor correto  """


sexo = str(input('Informe seu sexo [ M ] / [ F ]: ')).lower().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor informe seu sexo : ')).lower().upper()[0]


print(f'Ola , sexo informado foi {sexo}')