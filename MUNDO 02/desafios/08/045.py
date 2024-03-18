from random import randint



def jogar(itens, computador,jogador):
    if computador == 0 : #COMPUTADOR JOGOU PEDRA
        if jogador == 0:
            print('-='*11)
            print('EMPATE')
            print(f'COMPUTADOR JOGOU {itens[computador]}')
            print(f'JOGADOR JOGOU PEDRA')
            print('-='*11)
        elif jogador == 1 :
            print('-='*11)
            print('JOGADOR VENCEU')
            print(f'COMPUTADOR JOGOU {itens[computador]}')
            print(f'JOGADOR JOGOU PAPEL')
            print('-='*11)
        elif jogador ==2:
            print('-='*11)
            print('COMPUTADOR VENCEU')
            print(f'COMPUTADOR JOGOU {itens[computador]}')
            print(f'JOGADOR JOGOU TESOURA')
            print('-='*11)
        else:
            print('JOGADA INVALIDA')

    elif computador == 1 : #COMPUTADOR JOGOU PAPEL
        if jogador == 0:
            print('-='*11)
            print('COMPUTADOR VENCEU')
            print(f'COMPUTADOR JOGOU {itens[computador]}')
            print(f'JOGADOR JOGOU PEDRA')
            print('-='*11)
        elif jogador == 1 :
            print('-='*11)
            print('EMPATE')
            print(f'COMPUTADOR JOGOU {itens[computador]}')
            print(f'JOGADOR JOGOU PAPEL')
            print('-='*11)
        elif jogador ==2:
            print('-='*11)
            print('JOGADOR VENCEU')
            print(f'COMPUTADOR JOGOU {itens[computador]}')
            print(f'JOGADOR JOGOU TESOURA')
            print('-='*11)
        else:
            print('JOGADA INVALIDA')
    elif computador == 2 : #COMPUTADOR JOGOU TESOURA
        if jogador == 0:
            print('-='*11)
            print('JOGADOR VENCEU')        
            print(f'COMPUTADOR JOGOU {itens[computador]}')
            print(f'JOGADOR JOGOU PEDRA')
            print('-='*11)
        elif jogador == 1 :
            print('-='*11)
            print('COMPUTADOR VENCEU')        
            print(f'COMPUTADOR JOGOU {itens[computador]}')
            print(f'JOGADOR JOGOU PAPEL')
            print('-='*11)
        elif jogador ==2:
            print('-='*11)
            print('EMPATE')
            print(f'COMPUTADOR JOGOU {itens[computador]}')
            print(f'JOGADOR JOGOU TESOURA')
            print('-='*11)
        else:
            print('JOGADA INVALIDA')


def menu():
    while True:
        itens = ['PEDRA', 'PAPEL', 'TESOURA']
        computador = randint(0,2)
        print('-='*20)
        print('''Escolha sua jogada :\n 
        [ 0 ] - PEDRA\n      
        [ 1 ] - PAPEL\n
        [ 2 ] - TESOURA\n    
        [ 3 ] - SAIR
        ''')
        print('-='*20)
        jogador = int(input('QUAL E SUA JOGADA ? : '))
        if jogador == 0 :
            return jogar(itens, computador,jogador)
            
        elif jogador == 1 :
            return jogar(itens, computador,jogador)
        elif jogador == 2 :
            return jogar(itens, computador,jogador)
        elif jogador == 4:
            break
menu()