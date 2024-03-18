""" Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas estratégias de código.  """
n=s=0
while True:
    n = int(input('Digite um numero : '))    
    if n == 999:
        break
    s += n
print(f"A soma vale {s}")