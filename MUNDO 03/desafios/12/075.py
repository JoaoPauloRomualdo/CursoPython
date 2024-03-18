""" 
Desafio 75

Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla . No final mostre:

    * Quantas vezes apareceu o valor 9
    * Em que posição foi digitado o primeiro valor 3
    * quais foram os numeros pares """


valores = ()
for i in range(1,5):
    numero = int(input('Digite um valor: '))
    valores += (numero,)

print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores :
    print(f'O primeiro valor 3 apareceu na posição {valores.index(3)+1}')
else:
    print('O número 3 não foi digitado')
pares = 0
for pos ,i in enumerate(valores,start=1):
    if i % 2 == 0:
        pares+=1
        print(f'Os numeros pares apareceram na posição {pos} que foram {i}')    
if pares == 0 :
    print('Você não digitou nenhum numero par')