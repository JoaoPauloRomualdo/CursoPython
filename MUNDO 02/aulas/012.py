#------ CONDIÇÕES ANINHADAS --------
nome = str(input('Qual e seu nome'))

#estrutura de condições aninhadas 
if nome == 'joao':
    print('que nome bonito')

elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('Seu nome e bem popular no Brasil')

elif nome in 'ana claudia jessica juliana':
    print('belo nome feminino')
else:
    print('Seu nome e bem normal')

print(f'tenha um otimo dia {nome}')