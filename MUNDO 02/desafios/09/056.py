""" 056
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas . No final do programa mostre :
    .A media de idade do grupo
    .Qual e o nome do homem mais velho
    .Quantos mulheres tem menos de 20 anos """

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
tot_mulher = 0
for i in range(1,5):
    print(f'------- {i} Pessoa -------')
    nome = str(input('Nome : ')).strip()
    idade = int(input('Idade : '))
    sexo = str(input('Sexo [ M ] - Masculino , [ F ] - Feminino  ')). strip()

    soma_idade+= idade

    if i == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome

    if sexo in 'Mm' and idade > maior_idade_homem :
        maior_idade_homem = idade
        nome_velho = nome

    if sexo in 'Ff' and idade < 20 :
        tot_mulher += 1
media_idade = soma_idade/4
print(f'A media de idade do grupo e de {media_idade} anos')
print(f'O homem mais velhor tem {maior_idade_homem} , e o nome dele e {nome_velho}')
print(f'Ao todo são {tot_mulher} mulheres com menos de 20 anos')