""" 
Desafio 034

Escreva um programa que pergunte o salário de um funcionário e Calcule o valor do seu aumento

    .Para salários superiores a R$1250,00 calcule um aumento de 10%
    .Para os inferiores ou iguais o aumento é de 15% """

print('-' * 80)
salario = float(input('Digite o valor do salario que vai receber o aumento R$ : '))
print('-' * 80)

if salario >= 1250 :
    aumento = salario * (10/100)
    salario_final = salario + aumento
    print(f'O seu salairo e de R$: {salario} e seu aumento foi de 10% totalizando R$:{aumento} de aumento , seu salario final sera R$: {salario_final}')
else :
    aumento = salario * (15/100)
    salario_final = salario + aumento
    print(f'O seu salairo e de R$: {salario} e seu aumento foi de 15% totalizando R$:{aumento} de aumento , seu salario final sera R$: {salario_final}')
