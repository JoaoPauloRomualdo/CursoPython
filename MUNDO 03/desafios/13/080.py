""" 
Desafio 080

Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista , ja na posição correta de inserção (sem usar o sort()). No final , mostre a lista ordenadas na tela """
valores = []
for i in range(1,6):
    valor = int(input(f'Digite o {i}° valor : '))
    if valor in valores:
        print('Valor ja existente !!!')
        print('Tente novamente ....')
    else:
        posicao = 0
        while posicao < len(valores) and valores[posicao] < valor:
            posicao += 1
        valores.insert(posicao, valor)
        print('Valor adicionado com sucesso !!!')
print(f'Valores adicionados foram {valores}')