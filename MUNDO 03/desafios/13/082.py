""" Desafio 082

Crie um programa que vai ler varios numeros e colocar em uma lista . Depois disso crie duas listas extras que vao conter apenas os valores pares e os valores impares digitados respectivamente . Ao final mostre o conteudo das tres listas geradas """

numeros = []
pares = []
impar = []

while True:
    n = int(input('Digite um numero : '))
    numeros.append(n)
   
    if n % 2 == 0:
        pares.append(n)
    else :
        impar.append(n)

    resp = str(input('Deseja continuar ? [ S ] / [ N ] : ')).lower().strip()[0]
    while resp not in ['s', 'n']:
        print('Informe uma resposta vailda !!!')
        resp = str(input('Deseja continuar ? [ S ] / [ N ] : ')).lower().strip()[0]
    
    if resp == 'n':
        break
print(f'Você digitou os valores {numeros}')
print(f'Os numeros pares digitado foram {pares}')
print(f'Os numeros impares digitado foram {impar}')
    

