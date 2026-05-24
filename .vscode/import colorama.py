import colorama
from colorama import Fore, Style

# Inicializa a biblioteca colorama (necessário especialmente para Windows)
colorama.init()

# 1. Utilizar uma lista para armazenar as mensagens do reservatório
mensagens_reservatorio = [
    "Muito baixo (crítico)", # Nível 1 (Índice 0)
    "Baixo",                 # Nível 2 (Índice 1)
    "Médio",                 # Nível 3 (Índice 2)
    "Alto",                  # Nível 4 (Índice 3)
    "Muito alto (alerta)"    # Nível 5 (Índice 4)
]

# 2. Criar uma função responsável por definir a cor da mensagem conforme o nível
def exibir_alerta(nivel):
    # Verifica se o nível está dentro do limite (1 a 5)
    if 1 <= nivel <= 5:
        # Pega a mensagem correspondente na lista (subtrai 1 pois o índice começa em 0)
        situacao = mensagens_reservatorio[nivel - 1]
        
        # Define a cor de acordo com o nível
        if nivel == 1:
            cor = Fore.RED       # Vermelho
        elif nivel == 2:
            cor = Fore.YELLOW    # Amarelo
        elif nivel == 3:
            cor = Fore.GREEN     # Verde
        elif nivel == 4:
            cor = Fore.CYAN      # Ciano
        elif nivel == 5:
            cor = Fore.BLUE      # Azul
            
        # 3. Exibir no terminal a situação atual com a cor correspondente
        # 4. Restaurar o estilo padrão após a exibição (Style.RESET_ALL)
        print(f"{cor}Nível {nivel} do reservatório: {situacao}{Style.RESET_ALL}")
    else:
        print("Nível inválido. Informe um nível de 1 a 5.")

# --- Simulação do ambiente real de monitoramento ---
print("Iniciando simulação de monitoramento...\n")

# Valores definidos no código (sem entrada do usuário, conforme as orientações)
niveis_simulados = [1, 2, 3, 4, 5]

for nivel_atual in niveis_simulados:
    exibir_alerta(nivel_atual)

print("\nSimulação finalizada.")