amigos = {}
num_participantes = int(input("Quantos amigos irão partticipar do seu evento?"))
if num_participantes <= 0:
    print("Número inválido de participantes")
else:
    for amg in range(num_participantes):
        nome = input(f"Qual o nome do participante № {amg + 1}: ")
        item_dicionario = {nome: 0}
        amigos.update(item_dicionario)
print(f"Lista de participantes:")
for c, v in amigos.items():
    print(f"Nome: {c} | Conta: R${v}")
