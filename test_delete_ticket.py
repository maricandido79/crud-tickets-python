from tickets import deletar_ticket, carregar_tickets

# Deletar o ticket com ID 1
resultado = deletar_ticket(1)
print(resultado)

# Verificar todos os tickets depois da exclusão
tickets = carregar_tickets()
for t in tickets:
    print(f"ID: {t['id']}, Título: {t['titulo']}, Status: {t['status']}")
