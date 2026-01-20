from tickets import criar_ticket

# Ticket 1 (ID 1) já existe, só para referência
ticket1 = {
    "id": 1,
    "titulo": "Teste do sistema",
    "descricao": "Verificando JSON local",
    "status": "Aberto"
}

# Ticket 2 (novo ticket)
ticket2 = {
    "id": 2,
    "titulo": "Segundo teste",
    "descricao": "Verificando criação de outro ticket",
    "status": "Aberto"
}

# Tenta criar ambos
resultado1 = criar_ticket(ticket1)
resultado2 = criar_ticket(ticket2)

print(resultado1)
print(resultado2)
