from tickets import carregar_tickets

def listar_tickets():
    tickets = carregar_tickets()  # pega todos os tickets do JSON
    if not tickets:
        print("Nenhum ticket encontrado.")
        return
    for t in tickets:
        print(f"ID: {t['id']}, Título: {t['titulo']}, Status: {t['status']}")

# Executa a listagem quando rodar o arquivo
if __name__ == "__main__":
    listar_tickets()
