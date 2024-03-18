""" Desafio 068:

Faça um programa que jogar par ou impar com o computador. O jogo so sera interrompido quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo. """

from random import randint

numeroRandom = randint(0,10)


print('-=-'*15)
print('VAMOS JOGAR IMPAR OU PAR')
print('-=-'*15)

def jogo():
    usuario = int(input('Digite o seu numero que você deseja jogar : '))
    escolha = str(input('Você quer [ PAR ] ou [ IMPAR ] : ')).strip().upper()[0]
    resultado = numeroRandom + usuario
    tentativas = 0
    while True:
        if resultado % 2 == 0 :
            if escolha == 'I':
                print('-=-'*15)
                print()
                print(f'Que pena você perdeu, você teve {tentativas} vitoria consecutiva !!!')
                print(f'Você jogou {usuario} e o computador jogou {numeroRandom} o resultado deu {resultado}')
                print('O resultado deu PAR e você escolheu IMPAR')
                print()
                print('-=-'*15)
                break
            else:
                tentativas +=1

                print('-=-'*15)
                print()
                print('Parabéns você ganhou,vamos jogar novamente ')
                print(f'Você jogou {usuario} e o computador jogou {numeroRandom} o resultado deu {resultado}')
                print('O resultado deu PAR e o computador escolheu IMPAR')
                print()
                print('-=-'*15)
                return jogo()
        else:
            if escolha == 'P':
                print('-=-'*15)
                print()
                print(f'Que pena você perdeu, você teve {tentativas} vitoria consecutiva !!!')
                print(f'Você jogou {usuario} e o computador jogou {numeroRandom} o resultado deu {resultado}')
                print(f'O resultado deu IMPAR e você escolheu PAR !!!')
                print()
                print('-=-'*15)
                break
            else:
                tentativas +=1

                print('-=-'*15)
                print()
                print('Parabéns você ganhou, vamos jogar novamente ')
                print(f'Você jogou {usuario} e o computador jogou {numeroRandom} o resultado deu {resultado}')
                print('Resultado deu IMPAR e o computador escolheu PAR !!!')
                print()
                print('-=-'*15)
                return jogo()

jogo()