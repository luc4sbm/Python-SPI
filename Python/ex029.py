velocidade = int(input("Qual a velocidade atual do carro? "))
valor_multa = (velocidade - 80) * 7

if velocidade <= 80:
    print("Tenha um bom dia! Dirija com segurança!")
else:
    print("Multado! você excedeu o limite permitido que é de 80 Km/h")
    print(f"Você deve pagar uma multa de R$ {valor_multa:.2f}!")
