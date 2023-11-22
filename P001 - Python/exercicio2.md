# Operadores Aritméticos em Python
Em Python, os operadores aritméticos básicos são os mesmos que em C/C++, incluindo assim adição (+), subtração (-), multiplicação (*), divisão (/), divisão inteira (//), módulo (%), e exponenciação (**). Operadores compostos, como +=, -=, *=, /=, são suportados em Python da mesma forma que em C/C++.

# Exemplo de operadores aritméticos e compostos em Python
a = 10
b = 3

# Operadores aritméticos
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisao_inteira = a // b
modulo = a % b
exponenciacao = a ** b

# Operadores compostos
a += 1  # equivalente a a = a + 1
b -= 2  # equivalente a b = b - 2

# Representação de Números Inteiros Grandes
Python suporta inteiros arbitrariamente grandes, permitindo representar números muito grandes sem preocupação com os limites de armazenamento. Vamos comparar o fatorial de 30 com o maior valor inteiro representável em C/C++.

import math

fatorial_30 = math.factorial(30)
print("Fatorial de 30 em Python:", fatorial_30)

# Maior valor inteiro representável em C/C++ para sistemas de 32 bits
maior_inteiro_C = 2**31 - 1 
print("Maior inteiro em C/C++:", maior_inteiro_C)

# Variáveis Numéricas Imutáveis
As variáveis numéricas em Python são imutáveis, o que significa que, uma vez que você atribui um valor a uma variável, não pode modificá-la. Se você precisar de um novo valor, deve criar uma nova variável.

# Exemplo de variáveis numéricas imutáveis
x = 5
y = x  
y += 2  # isso não altera o valor de x

print("Valor de x:", x)  # saída de x continua sendo 5
print("Valor de y:", y)  # saída y somou x com 2

# Métodos Disponíveis para Variáveis Inteiras
Em Python, as variáveis inteiras pertencem à classe int. Alguns métodos úteis incluem:

# Exemplo de métodos disponíveis para variáveis inteiras
numero = 42

# Método para obter o valor absoluto
abs_numero = abs(numero)

# Método para converter para string
str_numero = str(numero)

# Método para verificar se é par
eh_par = numero % 2 == 0

print("Valor absoluto:", abs_numero)
print("Convertido para string:", str_numero)
print("É par?", eh_par)