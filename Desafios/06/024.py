""" Desafio 024
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO' """

name_city = input('Digite o nome de sua cidade')

if name_city.find('Santo') == -1:
    print(f'Ah que pena parece que sua cidade não começa com Santo')  
else :
    print(f'Nome da cidade  digitado foi {name_city}')
