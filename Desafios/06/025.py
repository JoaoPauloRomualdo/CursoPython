""" Desafio 025
Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' em seu nome
 """

name = input('Digite seu nome completo por favor')

new_name = name.lower()
if new_name.find('silva') == -1 :
    print(f'O nome digitado foi {name} e parece que seu sobrenome nao contem o nome Silva')
else :
    print(f'Parabens seu nome é : {new_name} e ele tem o nome Silva')