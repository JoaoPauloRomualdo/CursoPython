""" Desafio 022
Crie um programa que leia o nome completo de uma passoa e mostre:
    . O nome com todas as letras maiúsculas
    . O nome com todas minúsculas
    . Quantas letras ao todo (sem considrar os espaços)
    . Quantas letras tem o primeiro nome
 """

name = str(input('Digite seu nome completo : ')).strip()

print(f'Nome digitado foi {name}, seu nome em letras maiúsculas ira ficar {name.upper()}')
print(f'Seu nome em letras minúsculas ira ficar : {name.lower()}')
print(f'Seu nome tem ao todo {len(name) - name.count(" ")}letras')
print(f'Seu primeiro nome tem {name.find(" ")} letras')