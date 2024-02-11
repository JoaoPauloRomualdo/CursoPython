""" 
026 
Faça um programa que leia a frase pelo teclado e mostre :
    . Quantas vezes aparece a letra "A"
    . Em que posição ela aparece a primeira vez
    . Em que posição ela aparece a última vez
"""
txt = input('Digite algum tipo de texto')
new_txt = txt.lower()

print(f'O texto digitado foi {txt} ele contem {new_txt.count("a")} letra A')

print(f'A primeira letra A aparece na : {new_txt.find("a")} posição')

print(f'A ultima letra A aparece na : {new_txt.rfind("a")} posição')

