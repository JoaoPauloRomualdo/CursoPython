""" 
Exercício Python 037:
    Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. """

def binario(number):
    binario = bin(number)
    print(f'O número digitado foi {number}, sua conversão para base BINARIA : {binario}')

def octal (number):
    octal = oct(number)
    print(f'O número digitado foi {number}, sua conversão para base OCTAL : {octal}')

def hexadecimal (number):
    hexa = hex(number)
    print(f'O número digitado foi {number}, sua conversão para base OCTAL : {hexa}')

def all(number):
    all = [binario, octal,hexadecimal]
    print(all)

def menu() :        
    print('='*40)
    print('Olá Bem vindo ao nosso sistema de conversão de números\n BINARIOS , OCTAL E HEXADECIMAL')
    print('='*40)
    number = int(input('Agora digite o número que deseja realizar a conversão : '))
        
    while True:
        print()
        print('Escolha a opção desejada para a conversão')
        print('[1] - BINÁRIO')
        print('[2] - OCTAL')
        print('[3] - HEXADECIMAL')

        opcao = int(input('Digite a opção desejada : '))

        if opcao == 1 :
            binario(number)
        elif opcao == 4:
            all(number)
        else :
            break

menu()