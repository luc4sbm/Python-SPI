
numero1 = int(input('Digite um número: '))

print(f'Variável 1 tem o valor de: {numero1}')

numero2 = int(input('Digite outro número: '))

print(f'Variável 2 tem o valor de: {numero2}')

temp = numero1
numero1 = numero2
numero2 = temp

print(f'Agora a variável 1 tem o valor de: {numero1} \n e a variável 2 tem o valor de: {numero2}')