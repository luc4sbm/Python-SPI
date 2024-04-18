'''
numero = int(input("Digite um número inteiro entre 10 e 20: "))
binario_numero = bin(numero)
print(list(binario_numero[2:]))

'''

numero = int(input(""))
binario_numero = bin(numero)

if numero < 10 or numero > 20:
    print("O número inserido não está dentro do intervalo permitido.")
else:
    print(list(binario_numero[2:]))
