def imprimir_caracteres_numericos():
    # Utilizando um loop para percorrer os caracteres numéricos de '0' a '9'
    for i in range(10):
        char = chr(ord('0') + i)  # Obtendo o caractere numérico
        ascii_code = ord(char)     # Obtendo o código ASCII do caractere
        octal_code = oct(ascii_code)  # Obtendo o código em octal
        hex_code = hex(ascii_code)    # Obtendo o código em hexadecimal

        print(f"'{char}' - Decimal: {ascii_code}, Octal: {octal_code}, Hexadecimal: {hex_code}")

imprimir_caracteres_numericos()
