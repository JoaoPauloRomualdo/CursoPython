entrada_usuario = input("Digite algo: ")

# Tipo primitivo
tipo_primitivo = type(entrada_usuario)

# Informações sobre o tipo primitivo
informacoes_tipo = f"Informações sobre o tipo primitivo ({tipo_primitivo}):"

# Verifica se é uma string e adiciona informações adicionais
if tipo_primitivo == str:
    informacoes_tipo += f"\n- É uma string de comprimento {len(entrada_usuario)}."
    if entrada_usuario.isnumeric():
        informacoes_tipo += "\n- Contém apenas dígitos."
    elif entrada_usuario.isalpha():
        informacoes_tipo += "\n- Contém apenas letras."
    elif entrada_usuario.isalnum():
        informacoes_tipo += "\n- Contém letras e/ou dígitos."
    else:
        informacoes_tipo += "\n- Contém caracteres especiais."

# Exibe as informações
print(informacoes_tipo)

