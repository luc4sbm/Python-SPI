#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input("Me diga um número qualquer: "))

divisivel = 0 # essa variavel tem que ficar fora do loop pra não receber sempre o mesmo valor
for i in range (1, numero+1): # cria um loop que roda de 1 até o número digitado
    if numero % i == 0: #verificado se o número digitado é uma divisão inteira
        print(f"\033[93m{i}\033[0m", end=' ')
        divisivel += 1
    elif numero % i != 0:
        print(f"\033[91m{i}\033[0m",end=' ')  
print(f"\nO número {numero} foi divisível {divisivel} vezes")
if divisivel > 2:
    print("E por isso ele NÃO É PRIMO!")
else:
    print("E por isso ele É PRIMO!")          