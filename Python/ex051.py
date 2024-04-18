print('-=' * 10)
print("10 TERMOS DE UMA PA")
print('-=' * 10)
termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

for i in range (termo, termo + 10*razao, razao):
    print(i,end=' → ')
print("ACABOU")