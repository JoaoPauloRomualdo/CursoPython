""" Desafio 069 :

Crie um programa que leia a idade e o sexo de varias pessoas . A cada pessoa cadastrada , o programa devera perguntar se o usuario quer ou nao continuar no final mostre:
    *Quantas pessoas tem mais de 18 anos
    *Quantos homens foram cadastrados
    *Quantas mulheres tem menos de 20 anos """
print('='*20)
print('CADASTRO DE PESSOAS')
print('='*20)
print()
maiorIdade = cadHomens = mulheresMenores = 0
while True:
    print('_'*20)
    print()    
    idade = int(input('Digite sua idade : '))
    sexo = str(input('Informe seu sexo :  ')).strip().upper()[0]
    opcao = str(input('Você deseja continuar ? [ SIM ] - [ NÃO ]')).strip().upper()[0]
    print()

    if opcao == 'S':
        if idade > 18:
            maiorIdade +=1
        if sexo == 'M':
            cadHomens += 1
        if sexo in 'F' and idade < 18 :
            mulheresMenores += 1
    else:
        break

print(f'Total de pessoas com mais de 18 anos: {maiorIdade}')
print(f'Total de homens cadastrados: {cadHomens}')
print(f'Total de mulheres com menos de 18 anos: {mulheresMenores}')
