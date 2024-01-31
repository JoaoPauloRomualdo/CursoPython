""" 
Desafio 014
Faça um algoritmo que leia a temperatura em graus °C e converta para °F """

temperatura = float(input('Digite a temperatura em graus °C :'))


nova_temperatura = temperatura * 9/5 + 32

print(f'Temperatura em graus °C :{temperatura}, e a temperatura em °F : {nova_temperatura}')