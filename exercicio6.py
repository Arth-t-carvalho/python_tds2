import requests #biblioteca ára fazer requisiçoes http

cep = input("digite o cep(somente os numero):")
cep = cep.replace("-","")#vai tirar os tracinhos se o usuario digitar

if len(cep) !=8 or not cep.isdigit():
    print("cep invalido1!!! digite ate 8 numeros")
else:
    url = f"https://viacep.com.br/ws/{cep}/json"
    resposta = requests.get(url)
    dados = resposta.json()

if "erro" in dados:
    print("CEP nao encontrado")

