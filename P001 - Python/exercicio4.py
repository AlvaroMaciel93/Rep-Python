nome_completo = "Ana Maria"

# Utilizando o método split() para dividir a string em uma lista de palavras
partes_nome = nome_completo.split()

# Verificando se a lista tem pelo menos duas partes (nome e sobrenome)
if len(partes_nome) >= 2:
    nome = partes_nome[0]  # Primeiro elemento da lista é o nome
    sobrenome = partes_nome[-1]  # Último elemento da lista é o sobrenome

    # Verifique qual das duas novas variáveis antecede a outra na ordem alfabética
    if nome < sobrenome:
        print(f"{nome} antecede {sobrenome} na ordem alfabética")
    elif nome > sobrenome:
        print(f"{sobrenome} antecede {nome} na ordem alfabética")
    else:
        print("O nome e sobrenome são iguais na ordem alfabética")

    # Verifique a quantidade de caracteres de cada uma das novas variáveis
    print(f"Quantidade de caracteres no nome: {len(nome)}")
    print(f"Quantidade de caracteres no sobrenome: {len(sobrenome)}")

    # Verifique se seu nome é uma palíndromo
    nome_minusculo = nome.lower()  # Convertendo para minúsculas para evitar problemas de caso
    if nome_minusculo == nome_minusculo[::-1]:
        print(f"{nome} é um palíndromo!")
    else:
        print(f"{nome} não é um palíndromo.")
else:
    print("Não foi possível separar o nome do sobrenome. Verifique se inseriu o nome completo corretamente.")
