aparelho = input("Digite o nome do aparelho: ")
potencia = int(input("Digite a pontência do seu aparelho em watss (W): "))
horasDia = int(input("Digite o tempo médio de uso diário do seu aparelho em horas: "))

consumoMesal = (potencia * horasDia * 30)/1000
calculoCusto = consumoMesal*0.75

print(" ")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumoMesal} kWh/mês")
print(f"Custo estimado: R${calculoCusto:.2f}/mês")