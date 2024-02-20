""" Exercício Python 039: 
    Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. """
from datetime import datetime


colors = {
    'reset' : '\033[m',
    'red_color' : '\033[1;30;41m',
    'blue_color': '\033[1;30;46m',
    'yellow_color' : '\033[1;30;43m'
}

current_year = datetime.now().year
year = int(input('Digite o ano em que você nasceu : '))


new_year = current_year - year

if new_year == 18 :
    print(f'{colors["red_color"]} Fique atento você ja tem {new_year} anos o alistamento militar e OBRIGATORIO o prazo para o alistamento militar obrigatório termina em 30 de junho {colors["reset"]}')
elif new_year == 17 and new_year <= 18  :
    print(f'{colors["blue_color"]}Ola , você tem {new_year} anos e ainda não possue idade para o alistamento militar, mas tome cuidado o proximo ano ja será obrigatorio seu alistamento{colors["reset"]}')
elif new_year >= 18 :
    print(f'{colors["yellow_color"]} Você possue {new_year} anos , espero que esteja com seu alistamento em dia !!!{colors["reset"]}')
