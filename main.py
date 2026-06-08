# Projeto E-Circuito Sustentável
# Registro de coleta de lixo eletrônico

print("=== Registro de Coleta de Lixo Eletrônico ===")

registros = []

while True:
    tipo = input("Digite o tipo de resíduo (ou 'sair' para finalizar): ")

    if tipo.lower() == "sair":
        break

    quantidade = int(input("Digite a quantidade: "))

    registros.append((tipo, quantidade))

print("\nResumo da Coleta:")
for item in registros:
    print(f"Tipo: {item[0]} - Quantidade: {item[1]}")