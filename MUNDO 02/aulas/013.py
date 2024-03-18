#ESTRUTURA DE CONTROLE (ESTRUTURA DE REPETIÇÃO FOR)

""" for i in range(0,10):#Ira contar de 0 ate 9 
    print(i) """

    #CONTADOR EM PYTHON ELE IGNORA O ULTIMO NUMERO SE VOCÊ QUISER FAZER UMA CONTAGEM DE 1 ATE 6 DEVERA COLOCAR DE 1 ATE 7

""" for c in range(1,7):
    print(c)
print('FIM')
    
for i in range(6,0,-1):#NESSE EXEMPLO ESTAMOS COLOCANDO A INTERAÇÃO NO CASO ELE IRA COMECAR A CONTAR DE 6 SEMPRE TIRANDO 1 OU SEJA UMA CONTAGEM REGRESSIVA
    print(i)

print('FIM') """

""" n = int(input('Digite um número'))
for c in range(0,n+1):
    print(c*2)
print('fim') """

n = int(input('DIGITE O NUMERO DA TABUADA QUE DESEJA FAZER: '))

for i in range(1,11):
    tabuada = i * n
    print(f'{n} * {i} = {tabuada}')