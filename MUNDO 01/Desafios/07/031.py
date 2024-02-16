""" Desafio 031

Desenvolva um programa que pergunte a distancio de uma viagem em Km . Calcule o preço da passagem cobrando R$ 0,50 por km para viagen até 200Km e R$ 0,45 para viagens mais longas """

print('='*80)
print('DIGITE A DISTÂNCIA QUE VOCÊ PRETENDE VIAJAR !!!')
print('='*80)

distance = int(input('Informe a distância em Km : '))

if distance <= 200 :
    new_distance = distance * 0.50
    print(f'A distância digitada foi {distance}KM, você ira pagar um total de : R${new_distance:.2f}')

else :
    new_distance = distance * 0.45
    print(f'A distância digitada foi {distance}KM, você ira pagar um total de : R${new_distance:.2f}')