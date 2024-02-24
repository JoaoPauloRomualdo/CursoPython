""" 052
Faça um programa que leia um numero inteiro e diga se ele e ou nao um numero primo """

numero = int(input("Digite um número inteiro: "))

# Um número primo é maior que 1 e é divisível apenas por 1 e por ele mesmo
if numero > 1:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print(f"{numero} não é um número primo.")
            break
    else:
        print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
