""" 
Desafio 064 
Crie um programa que leia varios numeros inteiros pelo teclado . O programa so vai parar quando o usuario digitar o valor 999 que e a condição de parada .No final mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag) """

cont = 0
soma = 0
numero = 0

while cont != 999:
    cont = int(input('Digite um numero ou [999 para parar]: '))
    if cont != 999 :
        soma += cont
        numero += 1

print (f'Você digitou {numero} numeros e a soma entre eles foi {soma} ')