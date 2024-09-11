# função de cores para facilitar na visualização
from functions.color_function import yellow, green, red

# função para contar quantas vezes a letra "Aa" aparecem
def count_a(txt):
    count_lower = txt.count('a')
    count_upper = txt.count('A')
    return count_lower, count_upper

# Laço de repetição pro usuário verificar mais de uma farase ou palavra
while True:
  # armazenando frase ou palavra a ser analisada
  text = input(yellow("Digíte uma frase ou palavra: "))
  # chamando função e retornando a quantidade de vezes
  count_lower, count_upper = count_a(text)
  # condição para saber quantas vezes a letra "a" aparece
  if count_lower <= 0:
    print(red(f"A letra 'a' minúscula não aparece nenhuma vez."))
  else: 
    print(green(f"A letra 'a' minúscula aparece {count_lower} vez(es)."))
  # condição para saber quantas vezes a letra "A" aparece
  if count_upper <= 0:
    print(red(f"A letra 'A' maiúscula não aparece nenhuma vez."))
  else: 
    print(green(f"A letra 'A' maiúscula aparece {count_lower} vez(es)."))
  # Armazenando resposta do usuário
  response = input(yellow("Deseja continuar? [S/N] ")).upper().strip()[0] # métodos para pegarem apenas a primeira letra e deixar em maiúscula
  # Quebrando laço de repetição caso a resposta seja N
  if response == 'N':
      break  
