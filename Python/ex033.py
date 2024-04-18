n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))
menor_valor = 0 
maior_valor = 0
# calcula menor valor
if n1 < n2 and n1 < n3:
    menor_valor = n1
elif n2 < n1 and n2 < n3:    
    menor_valor = n2
elif n3 < n2 and n3 < n1: 
    menor_valor = n3   
# calcula maior valor
if n1 > n2 and n1 > n3:
    maior_valor = n1
elif n2 > n1 and n2 > n3:    
    maior_valor = n2
elif n3 > n2 and n3 > n1: 
    maior_valor = n3  

print(f"O menor valor digitado foi {menor_valor}")
print(f"O maior valor digitado foi {maior_valor}")    
