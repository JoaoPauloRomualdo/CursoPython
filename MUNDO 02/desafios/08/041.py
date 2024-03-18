""" Exercício Python 041: 
    A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
    - Até 9 anos: MIRIM
    - Até 14 anos: INFANTIL
    - Até 19 anos: JÚNIOR
    - Até 25 anos: SÊNIOR
    - Acima de 25 anos: MASTER """

from datetime import datetime

current_year = datetime.now().year

category = ['MIRIM', 'INFANTIL', 'JÚNIOR', 'SÊNIOR', 'MASTER']

year = int(input('Digite o ano de nascimento do atleta : '))

new_year = current_year - year

if new_year < 9 :
    print(f'O atleta nasceu {new_year}, é se enquadra na categoria {category[0]}')

elif 9 <=  new_year <= 14 :
    print(f'O alteta nasceu em {new_year}, é se enquadra na categoria {category[1]}')

elif 14 < new_year <= 19 :
    print(f'O atleta nasceu em {new_year}, é se enquadra na categoria {category[2]}')

elif 19 < new_year <= 25 :
    print(f'O atleta nasceu em {new_year}, é se enquadra na categoria {category[3]}')

else :
    print(f'O atleta nasceu em {new_year}, e se enquadra na categoria {category[4]}')