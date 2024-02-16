#Crie um programa que leia dois numeros e mostre a soma entre eles
print('Olá digite dois valores e vamos realizar a soma entre eles !!')

n1 = input('Digite um número :')

n2 = input('Digite outro número : ')


if n1.isdigit(): 
    soma = int(n1) + int(n2) 

    print('Seu resultado está pronto !!')

    print('A soma entre {} + {} = {}'.format(n1, n2, soma))
    
else:
    print('Verifique se você digitou um número valído')