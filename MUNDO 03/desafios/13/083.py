""" Desafio 083

Crie um programa que o usuario digite um expressao qualquer que use parenteses . Seu aplicativo devera analisar se a espressao passada esta com os parenteses abertos e fechado na ordem correta """
expr = str(input('Digite sua expressão : '))
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':  
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão esta valida')

else:
    print('Sua expressão esta errada')