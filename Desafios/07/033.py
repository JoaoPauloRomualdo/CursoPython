""" 
Desafio 033

Faça um programa que leia três números e mostre qual e o maior e qual e o menor . """
print('='*80)
print('DIGITE TRÊS NÚMEROS E VAMOS VERIFICAR QUAIS DELES E O MAIOR NÚMEERO !!!')
print('='*80)

first_number = float(input('Agora digite um número : '))
second_number = float(input('Digite o segundo número : '))
third_number = float(input('Digite o terceiro número : '))

if first_number > second_number and first_number > third_number: 
    greater_number = first_number

if second_number > first_number and second_number > third_number:
    greater_number = second_number

if third_number > first_number and third_number > second_number:
    greater_number = third_number

print(f'O maior número digitado foi : {greater_number}')