""" Desafio 025
Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' em seu nome
 """

name = str(input('Digite seu nome completo por favor')).strip()

new_name = name.lower()
#if new_name.find('silva') == -1 :
if 'silva' in new_name != True:
    print(f'Parabens seu nome é : {new_name} e ele tem o nome Silva')
else :
    print(f'O nome digitado foi {name} e parece que seu sobrenome nao contem o nome Silva')