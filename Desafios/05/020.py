""" 
Desafio 020

O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um program que leia o nome dos quatro alunos e mostre a ordem sorteada .

"""
from random import shuffle

aluno1 = input('Digite o nome do primeiro aluno : ')
aluno2 = input('Digite o nome do segundo aluno : ')
aluno3 = input('Digite o nome do terceiro aluno : ')
aluno4 = input('Digite o nome do quarto aluno : ')

sorteio = [aluno1, aluno2, aluno3, aluno4]
shuffle(sorteio)

print('A ordem de apresentação será')
print(sorteio)
