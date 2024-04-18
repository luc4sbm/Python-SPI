# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.


#inicializa os contadores
conta_peso = 0
maior = 0
menor = 0
#loop para verificar os pesos
for i in range(1,6):
    peso = float(input(f"Peso da {i}ª pessoa: "))
    #calcula maior peso
    if peso > maior:
        maior = peso
    #calcula o menor peso    
    elif peso < maior:
        menor = peso



print(f"O maior peso lido foi de {maior:.1f}Kg ")
print(f"O menor peso lido foi de {menor:.1f}Kg ")

        