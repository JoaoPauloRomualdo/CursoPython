""" Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while. """
print('GERADOR DE PA')
print('-='*10)
primeiro = int(input("Primerio termo : "))
razao = int(input('Razão da PA : '))

termo = primeiro
cont = 1

while cont <= 10 :
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1

print('Fim')