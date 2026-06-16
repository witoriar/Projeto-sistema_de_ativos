import json


ARQUIVO_BANCO = "banco.json"


def carregar_dados():

    try:

        with open(ARQUIVO_BANCO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        return {"ativos": []}


def salvar_dados(dados):

    with open(ARQUIVO_BANCO, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)