""" Exercício Python 043: 
    Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
    - IMC abaixo de 18,5: Abaixo do Peso
    - Entre 18,5 e 25: Peso Ideal
    - 25 até 30: Sobrepeso
    - 30 até 40: Obesidade
    - Acima de 40: Obesidade Mórbida """

colors = {
    'reset' : '\033[m',
    'red': '\033[1;31;41m',
    'yellow' : '\033[1;30;43m'
}
print('='*50)
print('CALCULADORA DE I M C ')
print('='*50)
print()

height = float(input('Digite sua altura CM : '))

weight = float(input('Informe seu peso KG: '))

imc = round(weight / pow(height /100, 2),2)

print("-"* 20)
print('TABELA DO IMC')
print("-"* 20)
print()
print("""
        < 16	    |  Magreza Grau III\n
        16,0 a 16,9 |  Magreza Grau II\n
        17,0 a 18,4 |  Magreza Grau I\n
        18,5 a 24,9 |  Adequado\n
        25,0 a 29,9 |  Pré-Obeso\n
        30,0 a 34,9 |  Obesidade Grau I\n
        35,0 a 39,9 |  Obesidade Grau II\n
        >= 40       |  Obesidade Grau III
    """)

if imc < 18.5 :
    print(f'{colors["yellow"]} Seu IMC e de {imc}, você esta abaixo do peso ideal ! {colors["reset"]}')

elif 18.5 <= imc <= 25:
    print(f'{colors["yellow"]} Seu IMC e de {imc}, você esta no peso ideal {colors["reset"]}')

elif 25 <= imc <= 30 :
    print(f'{colors["red"]} Seu IMC e de {imc}, você esta com sobrepeso {colors["reset"]}')

elif 30 <= imc <= 40 :
    print(f'{colors["red"]} Seu IMC e de {imc}, você esta com obesidade {colors["reset"]}')

elif imc >= 40 :
    print(f'{colors["red"]} Seu IMC e de {imc}, você esta com Obesidade Mórbida {colors["reset"]} ')

