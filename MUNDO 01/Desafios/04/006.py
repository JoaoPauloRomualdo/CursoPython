#Desafio 006
#Crie um algoritmo que leia um numero e mostre o seu dobro
#seu triplo e raiz quadrada

numero = int(input('Digite um número '))

dobro = numero * 2 

triplo = numero * 3

raiz = numero **(1/2)

print(f'Número digitado foi {numero}\n Seu dobro sera {dobro}\n Seu triplo sera {triplo}\n E raiz sera {raiz:.2f}')