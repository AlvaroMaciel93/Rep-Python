# Listas dos animais do Zodíaco Chinês
zodiaco_chines = [
    "Rato", "Boi", "Tigre", "Coelho", "Dragão", "Serpente",
    "Cavalo", "Cabra", "Macaco", "Galo", "Cão", "Porco" ]

# Ano inicial do ciclo do Zodíaco Chinês (Rato)
ano_inicial = 1924

# Solicita o ano de nascimento ao usuário
ano_nascimento = int(input("Digite o ano de nascimento: "))

# Calcula o índice do signo no ciclo do Zodíaco Chinês
indice = (ano_nascimento - ano_inicial) % 12

# Determina o signo correspondente ao ano de nascimento
signo = zodiaco_chines[indice]

# Mostra o signo correspondente ao usuário
print(f"O seu signo do Zodíaco Chinês é: {signo}")
