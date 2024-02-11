""" Desafio 027
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome sepadaramente
    Ex : Ana Maria de Souza
    primeiro = Ana
    ultimo = Souza """

name = str(input('Digite seu nome completo : ')).strip()

new_name = name.split()

print (f'Seu nome completo e {name}')

print (f'O seu primeiro nome e : {new_name[0]}')

print (f'O seu ultimo nome sera : {new_name[len(new_name)-1]}')
