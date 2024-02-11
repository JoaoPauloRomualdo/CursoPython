""" Desafio 022
Crie um programa que leia o nome completo de uma passoa e mostre:
    . O nome com todas as letras maiúsculas
    . O nome com todas minúsculas
    . Quantas letras ao todo (sem considrar os espaços)
    . Quantas letras tem o primeiro nome
 """

name = input(str('Digite seu nome completo : '))


print(f'Nome digitado foi {name}, seu nome em letras maiúsculas ira ficar {name.upper()}')
print(f'Seu nome em letras minúsculas ira ficar : {name.lower()}')

total_de_letras = len(name.replace(" ", ""))
print(f'Seu nome tem o total de {total_de_letras} letras')

primeiro_nome = name.split()[0]
print(f'Seu primeiro nome tem {len(primeiro_nome)}')
