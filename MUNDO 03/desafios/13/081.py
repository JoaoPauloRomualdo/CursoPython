""" Desafio 081

Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso mostre: 
    * Quantos numeros foram digitados
    * A lista de valores ordenada de forma decrescente.
    * Se o valor 5 foi digitado e esta ou nao na lista """

numeros = []

while True:
    n = int(input('Digite um número : '))
    numeros.append(n)
    resp = str(input('Deseja continuar adicionando numeros ? [ SIM ] - [ NÃO ] : ')).lower()[0]
    while resp not in ['s', 'n']:
        print('Informe uma resposta invalida !!!')
        resp = str('Deseja continuar adicionando numeros ? [ SIM ] - [ NÃO ] : ').lower()[0]
   
    if resp == 'n':
        break

print(f'Foram digitados {len(numeros)} na lista !')
numeros_ordenados = sorted(numeros, reverse=True)
print(f'Lista de forma decrescente {numeros_ordenados}')
if 5 in numeros :
    print(f'O valor 5 foi digitado em sua lista {numeros}')
else :
    print('O valor 5 não foi digitado em sua lista !!!')