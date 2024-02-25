""" 054
Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maoiridade e quantas ja são maiores  """

from datetime import datetime

current_year = datetime.now().year

new = []
older_age = []
minor = []
for i in range(1,8):
  
    age = int(input('Digite o ano de seu nascimento : '))
  
    current_age = current_year - age

    if  18 <= current_age <= 21 : 
        new.append(current_age)

    elif current_age >= 21:
        older_age.append(current_age)
    
    else:
        minor.append(current_age)

print(f'Existem {len(new)} de pesoas maiores de 18 anos , possue {len(older_age)} pessoas acima de 21 anos é {len(minor)} pessoas menores de idade')