import json

import requests

url = "https://restcountries.com/v3.1/all?fields=name,capital,currencies"
urlName = "https://restcountries.com/v3.1/name/bra"

def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print("Erro ao fazer requisição em: ", url)


def parsing(texto_da_resposta):
    try:
        return json.loads(texto_da_resposta)
    except:
        pritn("Erro ao fazer parsing")


def contagem_de_paises(todos_os_paises):
    return len(todos_os_paises)

def listar_paises(lista_paises):
    for pais in lista_paises:
        print(pais['name']['common'])


if __name__ == "__main__":
    texto_da_resposta = requisicao(url)
    if texto_da_resposta:
        texto_depois_do_parsing = parsing(texto_da_resposta)
        if texto_depois_do_parsing:
            listar_paises(texto_depois_do_parsing)