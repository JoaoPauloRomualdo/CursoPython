""" 
026 
Faça um programa que leia a frase pelo teclado e mostre :
    . Quantas vezes aparece a letra "A"
    . Em que posição ela aparece a primeira vez
    . Em que posição ela aparece a última vez
"""
txt = str(input('Digite algum tipo de texto')).strip()
new_txt = txt.lower()

print(f'O texto digitado foi {txt} ele contem {new_txt.count("a")} letra A')

print(f'A primeira letra A aparece na : {new_txt.find("a")+1} posição')

print(f'A ultima letra A aparece na : {new_txt.rfind("a")+1} posição')

