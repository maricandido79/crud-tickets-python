from tickets import atualizar_ticket, carregar_tickets

# Atualizando o ticket com ID 2
novos_dados = {
    "titulo": "Segundo teste atualizado",
    "status": "Fechado"
}

resultado = atualizar_ticket(2, novos_dados)
print(resultado)

# Verificar todos os tickets depois da atualização
tickets = carregar_tickets()
for t in tickets:
    print(f"ID: {t['id']}, Título: {t['titulo']}, Status: {t['status']}")
