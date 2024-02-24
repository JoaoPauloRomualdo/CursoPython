""" Desafio 046

Faça um programa que mostre na tela uma contagem regressiva para estouro de fogos de artifio inde de 10 ate 0 com uma pausa de um segundo entre eles. """

import time
print("-="*20)
print('Se preparem para os fogos de artificio')
print("-="*20)

for i in range(10,0, -1):
    time.sleep(1)
    print(i)
print('''✷ 　 　　 　 ·
     ˚ * .
 　 　　 * ⋆ 　 .
 · 　　 ⋆ 　　　 ˚ ˚ 　　 ✦
 　 ⋆ · 　 *
 　　　　 ⋆ ✧　 　 · 　 ✧　✵
 　 · ✵'''*5)