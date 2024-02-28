# ------ ESTRUTURA DE REPETIÇÃO WHILE -------
""" while not maca:
    if chao :
        paso
    if naotemchao:
        pula
    if moeda:
        pega
    
pega() """

""" 
c = 1

while c < 10 :
    print(c)
    c += 1

print('fim') """
""" 
n = 1
while n != 0 :
    n = int(input('Digite um numero : '))

print('fim')
 """
n = 1

par = impar = 0

while n != 0:
    n = int(input('Digite um valor : '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print (f"você digitou {par} numeros pares e {impar} numeros impares")