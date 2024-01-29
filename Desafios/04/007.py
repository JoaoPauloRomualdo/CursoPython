#Desafio 007
#Desenvolva um programa que leia as duas notas de um aluno,
#calcule a mostre a sua media 

nome_aluno = input('Informe o nome do aluno : ')

primeira_nota = float(input('Digite a primeira nota do aluno : '))

segunda_nota = float(input('Digite a segunda nota do aluno : '))

media = (primeira_nota + segunda_nota) / 2

print(f'O aluno {nome_aluno} sua primeira nota foi {primeira_nota},segunda nota do aluno {segunda_nota}, media do aluno sera {media} ')
if media >= 7 :
    print(f'O aluno foi aprovado !!')

else :
    print(f'O aluno foi reprovado !!')