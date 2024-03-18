""" Desafio 065
Crie um programa que leia varios numeros inteiros pelo teclado , No final da execução , mostre a media entre todos valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuario se ele quer ou nao continuar digitando valores """

soma = 0

quantidade_numero = 0

numero_maior = 0

numero_menor = 0

while True:
    
    numero = int(input('Digite um número : ')) 

    soma+= numero
    quantidade_numero +=1
    
    media = soma / quantidade_numero
   
    if quantidade_numero == 1:
        numero_maior = numero
        numero_menor = numero
    else:
        if numero > numero_maior:
            numero_maior = numero

        if numero < numero_menor:
            numero_menor = numero
        

    opcao = str(input('Você quer digitar mais valores [ S ]- SIM / [ N ]- NÃO : ')).lower()

    if opcao == 'n' :
        break


print(f'A soma dos valores digitados é {soma}, você digitou {quantidade_numero} números, o maior número foi {numero_maior}, o menor número foi {numero_menor}, a média entre eles foi {media}')
            