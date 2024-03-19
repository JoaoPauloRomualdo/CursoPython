""" Desafio 76

Crie um programa que tenha um tupla unica com nomes de produtos e seus respectivos preços na sequencia, No final mostre um listagem de preços organizando os dados de forma tubular """

produtos = ('Carretilha', 250.00, 'Vara ', 150.00, 'Caiaque', 5000.00, 'Iscas', 120.00)

nomes_produtos = tuple(i for i in produtos if isinstance(i,str))

valores_produtos = tuple(i for i in produtos if isinstance(i, float))

print('=-'*20)
print('ITEMS PARA COMPRA'.center(40))
print('=-'*20)

for pos , p in enumerate(nomes_produtos):
        
    preco = valores_produtos[pos]
    print(f'{pos} - {p} {"*" * 20} {preco}')