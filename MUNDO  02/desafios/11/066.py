""" Desafio 066:

Crie um programa que leia varios numeros inteiros pelo teclado. O progama so vai parar quando o usuario digitar o valor 999 que e a condição de padara . No final mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag) """

quantidade = soma = 0
while True:
    numero = int(input('Digite um número ou [ 999 ] para parar : '))

    if numero == 999 :
        break
    quantidade += 1
    soma += numero

print(f'A soma dos {quantidade} valores digitado será :{soma} ')