# Programa: Pesquisa de Opinião - TudoWeb
# Autor: seuNome_Ag8_DS (substitua pelo seu nome)

print("=== PESQUISA DE OPINIÃO - TUDO WEB ===\n")

# Inicialização das contadores
cont_excellent = 0
cont_good = 0
cont_bad = 0
cont_ruim = 0

# Laço FOR para realizar 50 entrevistas
for i in range(1, 51):
    print(f"\n--- Entrevista {i} de 50 ---")
    
    nome = input("Digite o nome do cliente: ").strip()
    
    while True:
        try:
            idade = int(input("Digite a idade do cliente: "))
            if idade <= 0:
                print("Idade deve ser maior que zero. Tente novamente.")
                continue
            break
        except ValueError:
            print("Por favor, digite uma idade válida (número inteiro).")
    
    print("\nQual sua opinião sobre o atendimento? (digite o número)")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    
    while True:
        try:
            opiniao = int(input("Digite sua escolha (1, 2 ou 3): "))
            if opiniao == 1:
                cont_excellent += 1
                print("Resposta registrada: EXCELENTE")
                break
            elif opiniao == 2:
                cont_good += 1
                print("Resposta registrada: BOM")
                break
            elif opiniao == 3:
                cont_ruim += 1
                print("Resposta registrada: RUIM")
                break
            else:
                print("Opção inválida! Digite apenas 1, 2 ou 3.")
        except ValueError:
            print("Por favor, digite um número (1, 2 ou 3).")

# Resultados finais
print("\n" + "="*50)
print("RESULTADOS DA PESQUISA DE OPINIÃO")
print("="*50)
print(f"Quantidade de respostas EXCELENTE: {cont_excellent}")
print(f"Quantidade de respostas RUIM: {cont_ruim}")
print(f"Total de entrevistas realizadas: 50")
print("="*50)

# Estrutura de decisão para interpretar o resultado
if cont_excellent > cont_ruim:
    print("✅ CONCLUSÃO: A maioria dos clientes está satisfeita com o atendimento!")
elif cont_ruim > cont_excellent:
    print("⚠️  CONCLUSÃO: Há um número preocupante de clientes insatisfeitos (RUIM).")
else:
    print("⚖️  CONCLUSÃO: O número de EXCELENTE e RUIM está empatado.")