import requests, json

id = input("Digite um número qualquer: ")

url = f'https://rickandmortyapi.com/api/character/{id}'

# a linha abaixo faz uma solicitação no endpoint da API que estamos usando
resposta = requests.get(url)

# a linha abaixo exibe todo o conteúdo que veio na resposta
# print(resposta.content)

# a linha abaixo converte o json de resposta em alguma estrutura que o python conheça
conteudo = json.loads(resposta.content)

print(type(conteudo)) # no nosso caso, a estrutura foi um dicionário, poderia ter sido outra

print(conteudo['name'])

if resposta.status_code == 200:
    print(f"O personagem de Rick and Morty correspondente ao seu numero é {conteudo['name']}")
else:
    print("que número legal")