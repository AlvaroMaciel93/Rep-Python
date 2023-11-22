# Em Python, os caracteres especiais como 'ç' e 'ã' são tratados como parte da codificação Unicode, que é uma forma de representação de caracteres que inclui
# uma ampla gama de símbolos, letras, dígitos e caracteres especiais. No código, você pode simplesmente usar esses caracteres especiais diretamente em strings.

def imprimir_info_caractere():
    # Exemplo com caracteres especiais 'ç' e 'ã'
    caractere1 = 'ç'
    caractere2 = 'ã'

    # Obtém o código ASCII dos caracteres especiais 'ç' e 'ã'
    ascii_code1 = ord(caractere1)
    ascii_code2 = ord(caractere2)

    # Obtém o código em octal e em hexadecimal dos caracteres especiais 'ç' e 'ã'
    octal_code1 = oct(ascii_code1)
    hex_code1 = hex(ascii_code1)
    octal_code2 = oct(ascii_code2)
    hex_code2 = hex(ascii_code2)

    # Imprime os caracteres especiais e seus códigos ASCII, octal e hexadecimal
    print(f"'{caractere1}' - Decimal: {ascii_code1}, Octal: {octal_code1}, Hexadecimal: {hex_code1}")
    print(f"'{caractere2}' - Decimal: {ascii_code2}, Octal: {octal_code2}, Hexadecimal: {hex_code2}")

imprimir_info_caractere()
