def imprimir_info_caractere():
    # Solicita ao usuário para inserir um caractere
    caractere = input("Insira um caractere: ")

    # Obtém o código ASCII do caractere inserido
    ascii_code = ord(caractere)

    # Obtém o código em octal e em hexadecimal
    octal_code = oct(ascii_code)
    hex_code = hex(ascii_code)

    print(f"'{caractere}' - Decimal: {ascii_code}, Octal: {octal_code}, Hexadecimal: {hex_code}")

imprimir_info_caractere