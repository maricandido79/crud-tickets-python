import json
import os

DATABASE_FILE = "usuarios.json"

def carregar_dados():
    if not os.path.exists(DATABASE_FILE):
        return []
    with open(DATABASE_FILE, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar_dados(dados):
    with open(DATABASE_FILE, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
