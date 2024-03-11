""" 
Desafio 067:

Faça um progama que mostre a tabuada de varios numeros um de cade vez para cada valor digitado pelo usuario. O programa sera interrompido quando o numero solicitado for negativo """


cont = 0
while True:
    numero = int(input('Digite o número da tabuada : '))
    cont = 0
    while cont < 10 :
        cont += 1
        resultado = numero * cont
        print(f'{numero} x {cont} = {resultado}')
        
    opcao = input('Deseja continuar? [SIM] - [NÃO]: ').strip().upper()
    if opcao == 'N':
        break  

 
