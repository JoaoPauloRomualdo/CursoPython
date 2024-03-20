""" Desafio 77
Crie um programa que tenha uma tupla com varias palavras (não usar acentos).Depois disso você deve mostrar para cada palavra quais sao as suas vogais """
palavras = ('Pescar', 'Andar de bike', 'Caminhar', 'Jogo', 'Estudar', 'Saude')

for p in palavras :
    print(f'\nNa palavra {p} possue as vogais: ', end=' ') 
    for letra in p :
        if letra.lower() in 'aeiou':
            print(letra , end=' ')
