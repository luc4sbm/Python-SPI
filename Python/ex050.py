#Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0 # essa variavel tem que ficar fora do loop pra não receber sempre o mesmo valor

for i in range (1,7): # range que conta de 1 a 6
    ler_numeros = int(input(f"Digite o {i} valor inteiro: "))
    if ler_numeros % 2 == 0: # verifica se o número é par
        soma += ler_numeros #se o número for par "soma" vai somar o valor quer está guardado dentro dela com o numero par que está em ler números
print(f"soma soma dos números pares digitados foi {soma}! ")        
