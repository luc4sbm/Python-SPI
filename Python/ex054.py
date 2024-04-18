#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

# Pega o ano atual
import time
este_ano = time.localtime().tm_year

# Inicializa os contadores
menor = 0
maior = 0

# Loop para pegar o ano de nascimento de cada pessoa
for i in range(1, 8):
    # Prompt que pede o ano de nascimento de cada pessoa
    idade = int(input(f"Digite o ano de nascimento da {i}ª pessoa: "))

    # verifica se a pessoa é menor ou maior de idade
    if este_ano - idade < 18:
        menor += 1
    else:
        maior += 1

# mosta o resultado final
print(f"Ao todo tivemos {menor} pessoas menores de idade.")
print(f"Ao todo tivemos {maior} pessoas maiores de idade.")