""" 
Desafio 071:

Crie um programa que simule o funcionamento de um caixa eletronico. No inicio pergunte ao usuario qual sera o valor a ser sacado (numero inteiro) e o programa vai informas quantas cedulas de cada valor serao entregue

    obs: considere que o caixa possui cedulas de R$50, R$20, R$10 e R$1 """

print('='*30)
print('{:30}'.format('BANCO JPDEV'))
print('='*30)

valor = int(input('Que valor você quer sacar ? R$: '))
total = valor
cedula = 50
totalCedula = 0
while True:
    if total >=  cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0 :
            print(f'Total de {totalCedula} cedúlas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        if total == 0:
            break

print('='*30)
print('Volte sempre ! Tenha um bom dia !')