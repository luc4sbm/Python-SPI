'''Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

frase = input("Digite a uma frase: ").upper().replace(' ','')
letras = list(frase) #separa cada letra como caractere em uma lista
contador_letras = len(letras) #conta as letras para atribuir ao for
letras_invertidas = '' # var definida fora do for para não perder os valores

for i in range(1, contador_letras+1): 
    letras_invertidas += letras[-i] #letras invertidas vai receber o ultimo caractere fora da variavel, depois de outro lop vai somar o valor que já tinha dentro da varíavel a o outro valor
print(f"O inverso de {frase} é {letras_invertidas}")

if letras_invertidas == frase:
    print(f"Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")    
