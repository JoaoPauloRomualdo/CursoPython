frase = "Curso em Video Python"

#Fatiamento de texto
print(frase[9])

print(frase[9:13])

print(frase[9:21])

print(frase[9:21:2])#ele vai do 9 ao 21 saltando de 2 em 2

print(frase[:5])#Vai fatiar do 0 ate o 5 pois nao passamos nenhum parametro inicial 

print(frase[15:])#Aqui indicamos o parametros inicial mas nao indicamos o parametro final ele vai iniciar do caracter 15 e vai ate o final

print(frase[9::3])# Vai fatiar de 3 em 3 mostrando apartir do parametro inicial ate o fim 

#funcao len vai analisar o comprimento de uma frase
print(len(frase))
#count ('o') ele vai contar quantas vezes aparece a letra O
print(frase.count('o'))
#count('o', 0, 13) ele vai inciar uma contagem com fatiamento apartir do parametro passado nesse caso do 0 ao 13 
print(frase.count('o', 0, 13))
#a função find ele vai porcurar as letras que vc passar como parametro ex: frase.find('deo')
print(frase.find('deo'))
#a funcao find quando vc passa um parametro inexistente ela vai retornar o valor -1 ex: frase.find('android')
print(frase.find('Android'))
#posso usar o operador in ele vai verificar se existe o parametro existente exemplor 'Curso' in frase 
print('Curso' in frase)

#========= TRANSFORMAÇÃO =========
#VIA DE REGRA UMA LISTRA STRING ELA E IMUTAVEL, MAS VC CONSEGUE MUDAR ELA ATRAVES DE METODOS 

#o metodo replace ele vai alterar o parametro passado exemplo frase.replace('Python', 'Android')
print(frase.replace('Python', 'Android'))

#o metodo upper irar transformar toda a string em maiusculo
print(frase.upper())

#o metodo lower ele mantem oq e minusculo e transforma tudo que for maiusculo em letras minusculas 
print(frase.lower())

#o metodo capitalize ele vai pegar a string toda e vai deixar em letras minusculas e so a primeira letra ira ficar em maiusculo
print(frase.capitalize())

#o metodo title ele vai analizar quantas palavras existe dentro da string e deixar as primeiras letras em maiusculo
print(frase.title())

#o metodo strip vai remover os espaços em brancos inuteis 
frase2 = '  Aprenda Python   '
print(frase2)
print(frase2.strip())
#o metodo rstrip irar remover os espaços em branco a direita
print(frase2.rstrip())
#0 metodo lstrip irar remover os espaços em branco da esquerda
print(frase2.lstrip())

#------ DIVISÃO ------ 

#o split vai dividir em pedaços os epaços em branco de uma string 
print(frase.split())

#o join ele vai juntar e prencher uma string a partir do parametro passado
print('-'.join(frase))