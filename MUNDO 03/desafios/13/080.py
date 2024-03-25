""" 
Desafio 080

Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista , ja na posição correta de inserção (sem usar o sort()). No final , mostre a lista ordenadas na tela """
valores = []
for i in range(0,5):
    n = int(input(f'Digite um valor : '))
    if i == 0 or n > valores[-1]:
        valores.append(n)
        print('Adicionado no final da lista')
    else:
        pos = 0
        while pos < len(valores) :
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Valor adicinado na posição {pos}')
                break
            pos += 1
print(f'Valores digitados em ordem foram {valores}')