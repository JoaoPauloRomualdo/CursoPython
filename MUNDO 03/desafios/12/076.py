""" Desafio 76

Crie um programa que tenha um tupla unica com nomes de produtos e seus respectivos preços na sequencia, No final mostre um listagem de preços organizando os dados de forma tubular """

produtos = ('Carretilha', 250.00, 'Vara ', 150.00, 'Caiaque', 5000.00, 'Iscas', 120.00)

print('=-'*20)
print('ITEMS PARA COMPRA'.center(40))
print('=-'*20)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}',end='')
    else:
        print(f'R$ {produtos[pos]:>8.2f}')
        