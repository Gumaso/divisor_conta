amigos = {}
num_participantes = int(input("Quantos amigos irão partticipar do seu evento?"))
if num_participantes <= 0:
    print("Número inválido de participantes")
else:
    for amg in range(num_participantes):
        nome = input(f"Qual o nome do participante № {amg + 1}: ")
        item_dicionario = {nome: 0}
        amigos.update(item_dicionario)

valor_conta = float(input("Qual o valor da conta total: R$"))
valor_a_ser_pago_individual = round(valor_conta / len(amigos), 2)
for nome in amigos:
    amigos[nome] = valor_a_ser_pago_individual
print(f"Lista de participantes:")
for c, v in amigos.items():
    print(f"Nome: {c} | Conta: R${v}")
