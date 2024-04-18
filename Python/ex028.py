import random
from time import sleep
print("--=--"*10)
print ("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("--=--"*10)

#gera um número aleatório na variável
numero_pensado = random.randint(0,5)

#solicita um valor ao usuário
numero = int(input(f"Em qual número eu pensei? "))

print ("Processando...")
sleep(2)

if numero < 0 or numero > 5:
    print(f"Por favor, digite um número entre 0 e 5")
elif numero == numero_pensado:
    print(f"Parabéns! Você conseguiu me vencer!")
else:
    print(f"Ganhei! pensei no número {numero_pensado} e não {numero}")
