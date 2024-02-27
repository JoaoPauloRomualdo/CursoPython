# Inicializa as variáveis
soma_idade = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ""
quantidade_mulheres_menos_20 = 0

# Loop para coletar informações sobre 4 pessoas
for i in range(4):
    print(f"\nDados da {i+1}ª pessoa:")
    
    # Coleta o nome
    nome = input('Digite o nome: ')
    
    # Coleta a idade
    idade = int(input('Digite a idade: '))
    soma_idade += idade
    
    # Coleta o sexo
    sexo = input('Digite o sexo [M/F]: ').upper()
    
    # Verifica se é homem e se é mais velho que o registrado anteriormente
    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    
    # Verifica se é mulher com menos de 20 anos
    if sexo == 'F' and idade < 20:
        quantidade_mulheres_menos_20 += 1

# Calcula a média de idade
media_idade = soma_idade / 4

# Exibe os resultados
print("\nResultados:")
print(f"Média de idade do grupo: {media_idade:.2f} anos")

if nome_homem_mais_velho:
    print(f"Nome do homem mais velho: {nome_homem_mais_velho}")
else:
    print("Não há homens no grupo.")

print(f"Quantidade de mulheres com menos de 20 anos: {quantidade_mulheres_menos_20}")
