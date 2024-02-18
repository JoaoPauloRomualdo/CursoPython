""" 
Exercício Python 040: 
    Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
    - Média abaixo de 5.0: REPROVADO
    - Média entre 5.0 e 6.9: RECUPERAÇÃO
    - Média 7.0 ou superior: APROVADO """

colors = {
    'reset' : '\033[m',
    'red' : '\033[1;30;41m',
    'blue' : '\033[1;30;46m',
    'yellow' : '\033[1;30;43m'
}

name = str(input('Digite o nome do aluno : '))
first_media = float(input('Digite a primeira nota do aluno : '))
second_media = float(input('Digite a segunda nota do anluno : '))

media = (first_media + second_media) / 2

if media <= 5.0 :
    print(f'{colors["red"]}O aluno {name}, as notas do aluno foram {first_media}, {second_media}, infelizmente o aluno esta REPROVADO com uma media de {media} {colors["reset"]}')
elif media >= 5.0 and media <= 6.9 : 
    print(f'{colors["yellow"]}O aluno {name}, as notas do aluno foram {first_media}, {second_media}, este aluno esta de RECUPERAÇÃO com uma media de {media} {colors["reset"]}')
elif media >= 7.0 :
    print(f'{colors["blue"]}O aluno {name}, as notas do aluno foram {first_media}, {second_media}, esta aluno esta APROVADO  com uma media de {media} {colors["reset"]}')
