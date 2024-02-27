""" 053
Crie um programa que leia uma frase qualquer e diga se ela e uma palindroma desiderando os espaços .
Ex: Apos a sopa, são palavras que sao lidas de tras pra frente e sao a mesma coisa  """

frase = input("Digite uma frase: ").lower()  # Convertendo para minúsculas para garantir a comparação correta

# Removendo os espaços da frase
frase_sem_espacos = ''.join(frase.split())

# Verificando se a frase sem espaços é um palíndromo
if frase_sem_espacos == frase_sem_espacos[::-1]:
    print(f'A frase digitada foi {frase}')
    print("A frase é um palíndromo.")
else:
    print(f'A frase digitada foi {frase}')
    print("A frase não é um palíndromo.")
