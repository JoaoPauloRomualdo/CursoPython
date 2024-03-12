""" Desafio 070:

Crie um programa que leia o nome e o preço de varios produtos.O programa devera perguntar se o usuario quer continuar , No final mostre : 
    *Qual e o total gasto na compra
    *Quantos produtos custam mais de R$1000
    *Qual e o nome do produto mais barato """

print('*' * 40)
print(f'Bem-Vindo, a nossa lista de produtos'.center(40))
print('*' * 40)
total = prodCaro  = 0
prodBarato = float('inf')
nomeProdutoBarato = ''
while True:
    nomeProduto = str(input('Digite o nome do produto : '))
    preco = float(input('Qual o valor do produto R$: '))
    total += preco
    opcao = str(input('Deseja cadastrar mais produtos ? [ S ]- SIM / [ N ]- NÃO : ')).strip().lower()

    if preco >= 1000 :
        prodCaro += 1
    
    if preco < prodBarato:
        prodBarato = preco
        nomeProdutoBarato = nomeProduto
        
    while opcao != 's' and opcao != 'n':
        print('Resposta inválida. Por favor, responda com "Sim" ou "Não".')
        opcao = str(input('Deseja cadastrar mais produtos ? [ S ]- SIM / [ N ]- NÃO : ')).strip().lower()
    
    
    if opcao == 'n':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'Total gasto R${total:.2f}')
print(f"Total de produtos acima de R$1000,00 = {prodCaro}")
print(f'Nome do produto mais barato: {nomeProdutoBarato} (R${prodBarato:.2f})')