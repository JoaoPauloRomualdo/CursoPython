"""
OPERADORES ARITIMETICOS
=====================
+ adição
    5 + 2 == 7
- subtraçaõ
    5 - 2 == 3
* multiplicação
    5 * 2 == 10
/ divisão
    5 / 2 == 2.5
** potencia
    5 ** 2 == 25
// divisao inteira
    5 // 2 == 2
% Resto da divisão 
    5 % 2 == 1
=======================    
ORDEM DE PRECEDENCIA 

1 = []

2 = **

3 = *, /, //, % 

4 = + -

"""

soma = 5 + 3 * 2
print(soma)

b = 3 * 5 + 4 ** 2 
print (b)


c = 3 * (5+4) ** 2
print(c)

#MANEIRAS DE CALCULAR A RAIZ 
pontencia = pow(4,3)
print(pontencia)

#calcular a raiz de algum numero e mesma coisa de elevar o numero a 1/2
raiz = 81 ** (1/2)
print(raiz)

cubica = 127 ** (1/3)
print (cubica)

#Maneiras de repetir varias mensagem
msg = '=' *35
print (msg)
print('='*20)

nome = input('qual e seu nome')
#Alinhado a direita
print('Prazer em te conhecer {:>20}'.format(nome))
#Alinhado a esquerda
print('Prazer em te conhecer {:<20}'.format(nome))
#Alinhado ao centro
print('Prazer em te conhecer {:^20}'.format(nome))
#Alinhado ao centro e colocar algum caracter especial em volta
print('Prazer em te conhecer {:=^20}'.format(nome))


n1 = int(input('Digite um numero'))
n2 = int(input('Digite outro numero'))
soma = n1 + n2
mult = n1 * n2
div = n1 / n2
divInt = n1 // n2
pot = n1 ** n2

# :.3f significa que o resultado vai ser mostrado 3 casas apos a virgula com numero flutuante
print ('A soma e {},\n o produtu e {},\n a divisao e {:.3f}'.format(soma, mult , div),end=' ') # end ='' sigifinica que dois prints sera mostrado na msm linha de codigo
#\n ele vai quebrar a linha
print ('Divisao inteira {} e potencia {}'.format(divInt, pot))

