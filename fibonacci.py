# função de cores para facilitar na visualização
from functions.color_function import yellow, green, red

# Função para verificar se o número é de Fibonacci
def fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num or num == 0

# Laço de repetição para o usuário verificar mais de um número
while True:
    # Armazenando o número a ser analisado
    numero = int((input(yellow("Digite um número: "))))
    # Condição chamando a função para verificar se o número é de Fibonacci
    if fibonacci(numero):
        print(green(f"O número {numero} pertence à sequência de Fibonacci."))
    else:
        print(red(f"O número {numero} NÃO pertence à sequência de Fibonacci."))
    
    # Armazenando a resposta do usuário para ver se quer continuar
    response = input(yellow("Deseja continuar? [S/N] ")).upper().strip()[0] #  métodos para pegar apenas a primeira letra da resposta e deixar em maúsculas para ajudar na validação
    
    # Quebrando o laço de repetição caso a resposta seja 'N'
    if response == 'N':
        break
