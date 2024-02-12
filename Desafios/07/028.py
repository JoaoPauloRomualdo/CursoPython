""" Desafio 028

Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usúario tentar descobrir qual foi o número escolhido pelo computador
    .o programa deverá escrever na tela se o usúario venceu ou perdeu """

import random
from time import sleep
random_number = random.randint(1, 5)
print('Digite um número de 1 a 5 e veja se você adivinhou o numero que a maquina pensou !!')
print('-' * 70)
user_number = int(input('AGORA DIGITE UM NUMERO : '))
print('PROCESSANDO ....')
sleep(2)
#Verifica se o usuario digitou um numero entre 1 ao 5
if 1 <= user_number <= 5 :
    if random_number == user_number :
        print(f'PARABÉNS ! ! O número que a máquina pensou foi {random_number} e você acertou {user_number}')
    else :
        print(f'A QUE PENA ! !, A maquina pensou no {random_number} e você digitou {user_number}')
        print('MAIS SORTE DA PROXIMA VEZ !!!')
else :
    print('ATENÇÃO O NÚMERO DEVE SER DE 1 A 5')