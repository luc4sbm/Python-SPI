numero = int(input("Digite um número inteiro entre 10 e 20: "))
binario_numero = bin(numero)
bin_string = str(binario_numero[2:])
print(list(bin_string))
