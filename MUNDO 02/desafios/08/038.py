""" 
Exercício Python 038: 
    Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
    - O primeiro valor é maior
    - O segundo valor é maior
    - Não existe valor maior, os dois são iguais """

first_number = int(input('Digite um número : '))
second_number = int(input('Digite outro número : '))

if first_number > second_number :
    print(f'O maoir número entre {first_number} e {second_number} e : {first_number}')
elif second_number > first_number:
    print(f'O maior número entre {first_number} e {second_number} e : {second_number}')
elif first_number == second_number :
    print(f'Não existe maior número os dois numeros digitados são iguais {first_number} e {second_number}')
