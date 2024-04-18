import datetime
ano_nascimento = int(input("Ano de nascimento: "))
idade = date.today().year - ano_nascimento 
print(f"O atleta tem {idade} anos.")

if idade <= 9:
  print("Classificação: MIRIM")
elif idade > 9 and idade <= 14:
  print("Classificação: INFANTIL")
elif idade > 14 and idade <= 19:
  print("Classificação: JUNIOR")
elif idade > 19 and idade <= 25: 
  print("Classificação: SÊNIOR")
elif idade > 25:
  print("Classificação: MASTER")
