""" Desafio 057
Faça um programa que leia o sexo de uma pessoa, mas so aceite os valores 'M' ou 'F'.Caso esteja errado , peça a digitação novamente ate ter um valor correto  """



cont = 1
nome = str(input('Digite seu nome : '))

while cont != 0:
    sexo = str(input('Informe seu sexo [ M ] / [ F ]: ')).lower()

    if sexo == 'm':
        novo_sexo = 'Masculino'
    if sexo =='f':
        novo_sexo = 'Feminino'

        if sexo == 'm' or sexo == 'f':
            cont = 0
        else :
            print('Parece que ouve um erro na hora de informar seu sexo ')

print(f'Ola {nome} , sexo informado foi {novo_sexo}')