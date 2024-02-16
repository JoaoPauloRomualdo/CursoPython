""" Desafio 013

Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento """

salario = float(input('Digite o valor do salario que ira receber o aumento'))

adicional = salario * (15/100)

novo_salario = salario + adicional

print(f'O valor do salario digitado foi : R${salario}, valor do aumento aplicado :R${adicional}, valor do novo salario reajustado sera : R${novo_salario}')