from colorama import init, Fore, Style

init()

niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

def obter_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE

print("=== Monitoramento do Reservatório ===\n")

i = 2  # (0 = nível1, 1 = nível 2, 2 = nível 3, 3 = nível4, 4 = nível 5)
cor = obter_cor(i + 1)
print(cor + f"Nível {i + 1}: {niveis[i]}")

