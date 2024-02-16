#Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possiveis sobre ele
print('Olá vamos analisar que tipo de dado foi digitado por você, é iremos mostrar qual o tipo primitivo dele!!')

entradaUsuario = input('Agora digite alguma coisa : ')

print(type(entradaUsuario))

tipoInfo = entradaUsuario

if tipoInfo.isalpha():
        print("Você digitou apenas letras")

elif tipoInfo.isnumeric():
        print('Você digitou apenas números')

elif tipoInfo.isalnum():
        print('Você digitou letras e números')

else:
        print('Parece que você digitou caracteres especias')

print(tipoInfo)
#isnumeric() Somente numero
#isalpha() Somente letras
#isalnum() Letras e numero