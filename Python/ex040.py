nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) / 2 
print(f"Tirando {nota1:.1f} e {nota2:.1f} a média do aluno é {media}")
if media >= 7:
  print("O aluno está APROVADO!")
elif media > 5 and media < 7:
  print("Está de RECUPERAÇÃO mas ainda dá pra salvar!")
else: 
  print("REPROVADO!!!!! BURRÃO !!!!!")  