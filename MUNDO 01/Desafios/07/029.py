""" Desafio 029

Escreva um programa que leia a velocidade de um carro 
    .se ele ultrapassar 80Km/h mostre uma mensagem dizendo que ele foi multado 

    .a multa vai custar R$ 7,00 por cada km acima do limite """

print('-' * 80)
print(f'INFORME SUA VELOCIDADE !!!')
print('-' * 80)

speed = int(input('Digite sua velocidade KM : '))
#Verificando se a velocidade está maoir ou igual a 80 km/h
if speed >= 80 :
    new_speed = speed - 80
    fine = new_speed * 7
    print(f'VOCÊ FOI MULTADO UTRAPASSOU O LIMETE MAXIMO DE VELOCIDADE DE 80Km, SUA VELOCIDADE ERA DE : {speed}KM/H')
    print(f'SUA MULTA SERA DE R${fine:.2f}')
else :
    print(f'PARABÉNS !!! VOCÊ ESTÁ DENTRO DA VELOCIDADE PERMITIDA {speed}')