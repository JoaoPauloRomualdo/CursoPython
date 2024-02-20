""" Exercício Python 045: 
    Crie um programa que faça o computador jogar Jokenpô com você. """
import random


def jogar_jokenpo(escolha):
    opcoes = [1,2,3]
    maquina = random.choice(opcoes)
    if escolha == 1 :
        print(f'Você escolheu : {escolha} pedra')
        print(f'O computador escolheu : {maquina}')
    elif escolha == 2 :
        print(f'Você escolheu : {escolha} papel')
        print(f'O computador escolheu : {maquina}')
    elif escolha == 3:
        print(f'Você escolheu : {escolha} tesoura')
        print(f'O computador escolheu : {maquina}')

        if escolha == maquina :
            print(f'Você escolheu {escolha} e o computador {maquina} deu EMPATE')
        
        elif (escolha == 1 and maquina == 3) or \
            (escolha == 2 and maquina == 1) or \
            (escolha == 3 and maquina == 2):
            print("Você ganhou!")
        else:
            print('Voce perdeu')

while True:
    print("="* 30)
    print('BEM VINDO AO JOKENPÔ')
    print("="* 30)
    print('Escolha uma dessas opções para você jogar : ')
    print(f'[1] - Pedra ')
    print(f'[2] - Papel ')
    print(f'[3] - Tesoura ')
    print('[4] - Sair ')
    escolha = int(input('Digite a opção desejada : '))
    if escolha == 4 :
        print('Obrigado por jogar')
        break
    if escolha not in [1,2,3]:
        continue
    
    jogar_jokenpo(escolha)