def imprimir_caracteres_numericos():
    # Utilizando um loop para percorrer os caracteres numéricos de '0' a '9'
    for i in range(10):
        char = chr(ord('0') + i)  # Obtendo o caractere numérico
        ascii_code = ord(char)     # Obtendo o código ASCII do caractere

        # Imprimindo o caractere e seu código ASCII separados por ' - '
        print(f"'{char}' - {ascii_code}")

imprimir_caracteres_numericos()