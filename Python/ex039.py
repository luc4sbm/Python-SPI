from datetime import date
ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = date.today().year

idade = ano_atual - ano_nascimento
anos_faltantes = 18 - idade
ano_alistamento = ano_nascimento + 18


print(f"Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}. ")
if idade == 18:
  print("Você tem que se alistar IMEDIATAMENTE!")
elif idade < 18:
  print(f"Ainda faltam {anos_faltantes} para seu alistamento.")  
  print(f"Seu alistamento será em {ano_alistamento}")
elif idade > 18:
  print(f"Você já deveria ter se alistado a {ano_atual - ano_alistamento} anos")
  print(f"Seu alistamento foi em {ano_alistamento}")

