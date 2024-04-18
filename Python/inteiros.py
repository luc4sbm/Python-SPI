
numero = int(input("Digite um número inteiro entre 100 e 1000: "))
resto = numero % 5

if numero < 100 or numero > 1000:
    
    print("Por favor, insira um número inteiro positivo entre 100 e 1000")
else:
    print(f"O resto da divisão de {numero} por 5 é {resto}.")
  