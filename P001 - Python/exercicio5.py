#Operadores aritméticos e compostos em Python:

# Operadores aritméticos
a = 5.0
b = 2.0

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)

# Operadores aritméticos compostos
c = 3.0
c += 2.0  # Equivalente a c = c + 2.0
print("Valor de c após adição composta:", c)

#Utilizando o operador de exponenciação mostre qual a maior e a menor potência de 2 que pode ser representada com variáveis de ponto flutuante.

import sys

menor_potencia_de_2 = sys.float_info.min
maior_potencia_de_2 = sys.float_info.max

print("Menor potência de 2 representável:", menor_potencia_de_2)
print("Maior potência de 2 representável:", maior_potencia_de_2)

#Implicações da imutabilidade das variáveis numéricas:

x = 10.0
y = x
x += 5.0

print("Valor de x:", x)  # Mostra 15.0
print("Valor de y:", y)  # Mostra 10.0 (y permaneceu inalterado

#Métodos disponíveis para variáveis de ponto flutuante: as_integer_ratio(), is_integer(), hex().

z = 3.14
print(z.as_integer_ratio())  # Saída: (7070651414971679, 2251799813685248)
print(z.hex())  # Saída: '0x1.91eb851eb851fp+1'
print(z.is_integer())  # Saída: False
