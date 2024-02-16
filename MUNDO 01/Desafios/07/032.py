""" Faça um programa que leia um ano qualquer e mostre se ele e bissexto """
from datetime import date
ano = int(input('Que ano você quer analisar ? Digite zero para analisar o ano atual'))

if ano == 0 :
    ano = date.today().year
if ano % 4 == 0 and ano % 100 or ano % 400:
    print(f'O ano {ano} e BISSEXTO')
else:
    print(f'O ano {ano} não e BISSEXTO')