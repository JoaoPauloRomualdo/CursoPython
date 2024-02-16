""" Desafio 019

um professor quer sortear um dos seus quatros alunos para apagar o quadro . Faça um programa que ajude ele lendo o nomedeles e escrevendo  o nome do escolhido """

import random

aluno1 = input('Digite o nome do primeiro aluno : ')
aluno2 = input('Digite o nome do segundo aluno : ')
aluno3 = input('Digite o nome do terceiro aluno : ')
aluno4 = input('Digite o nome do quarto aluno : ')

sorteio = [aluno1, aluno2, aluno3, aluno4]

aluno_escolhido = random.choice(sorteio)

print(aluno_escolhido)