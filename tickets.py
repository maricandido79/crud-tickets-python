# Deletar ticket existente
def deletar_ticket(ticket_id):
    tickets = carregar_tickets()
    for i, t in enumerate(tickets):
        if t["id"] == ticket_id:
            deletado = tickets.pop(i)
            salvar_tickets(tickets)
            return {"mensagem": "Ticket deletado com sucesso", "ticket": deletado}
    return {"mensagem": "Erro: Ticket não encontrado", "id": ticket_id}
# Atualizar ticket existente
def atualizar_ticket(ticket_id, novos_dados):
    tickets = carregar_tickets()
    for t in tickets:
        if t["id"] == ticket_id:
            t.update(novos_dados)
            salvar_tickets(tickets)
            return {"mensagem": "Ticket atualizado com sucesso", "ticket": t}
    return {"mensagem": "Erro: Ticket não encontrado", "id": ticket_id}
import json
import os

TICKETS_FILE = "tickets.json"

def carregar_tickets():
    if not os.path.exists(TICKETS_FILE):
        return []
    with open(TICKETS_FILE, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar_tickets(tickets):
    with open(TICKETS_FILE, "w", encoding="utf-8") as arquivo:
        json.dump(tickets, arquivo, indent=4, ensure_ascii=False)

def criar_ticket(ticket):
    tickets = carregar_tickets()
    
    # verifica duplicação
    for t in tickets:
        if t["id"] == ticket["id"]:
            return {"mensagem": "Erro: Ticket com esse ID já existe", "ticket": ticket}

    tickets.append(ticket)
    salvar_tickets(tickets)
    return {"mensagem": "Ticket criado com sucesso", "ticket": ticket}
