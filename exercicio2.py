nome = input("digite o nome da plataforma")
horas = float(input("digite a quantidade de horas que vc assiste por semana:"))
preco = float(input("digite o preço da sua plataforma:"))
print(f"o valor mensal da assinatura {nome} é de {preco/(horas*4)}")
