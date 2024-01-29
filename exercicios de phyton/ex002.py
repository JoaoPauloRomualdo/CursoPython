#Crie um programa que de pergunte o nome de um usuario e de mensagem de boas vindas a ele
nomeUsu = input('Olá qual e seu nome ? ')

if len(nomeUsu) == 0:
    print('ATENÇÃO O CAMPO NOME TEM QUE SER PREENCHIDO')

else:
    print('Ola seja Bem-vindo, {}!'.format(nomeUsu))
