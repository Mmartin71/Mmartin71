# Pesquisa de Satisfação - TudoWeb

excelente = 0
bom = 0
ruim = 0

for i in range(1, 51):

    print("\nEntrevistado", i)

    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")

    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    opiniao = int(input("Digite a opção: "))

    if opiniao == 1:
        excelente = excelente + 1
    elif opiniao == 2:
        bom = bom + 1
    else:
        ruim = ruim + 1

print("\n--- RESULTADO DA PESQUISA ---")
print("Total de EXCELENTE:", excelente)
print("Total de BOM:", bom)
print("Total de RUIM:", ruim)