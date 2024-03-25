""" 
Desafio 079

Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista . Caso o  numero ja exista la dentro, ele nao sera adicionado.No final serão exibidos todos  os valores unicos digitados em ordem crescente """

numeros = []

while True:
    valor = int(input('Digite um valor : '))

    if valor not in numeros :
        numeros.append(valor)
        print('Valor adicionado com sucesso !!!')
    else :
        print('Valor ja existente, não irei adicionar !!!')

    resposta = str(input('Deseja continuar ? [ SIM ] - [ NÃO ]: ')).lower()[0]
    while resposta != 'n' and resposta != 's':
        print('Resposta invalida...')
        resposta = str(input('Deseja continuar ? [ SIM ] - [ NÃO ]: ')).lower()[0]

    if resposta == 'n':
        break

print(f'Você digitou os valores {numeros}')
print(f'Sua lista ordenada sera : {sorted(numeros)}')