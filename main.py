import random
import time


# Função para calcular o valor dividido de cada pessoa (sorteio)
def valor_dividido_sorteio(valor, lista_amigos):
    valor_a_ser_pago_individual = round(valor / (len(lista_amigos) - 1), 2)
    return valor_a_ser_pago_individual


# Função para calcular o valor dividido de cada pessoa (sem sorteio)
def valor_dividido_normal(valor, lista_amigos):
    valor_a_ser_pago_individual = round(valor / len(lista_amigos), 2)
    return valor_a_ser_pago_individual


# Dicionário que armazenará os amigos e seus valores a serem pagos
amigos = {}

# Pergunta ao usuário o número de participantes do evento
num_participantes = int(input("Quantos amigos irão participar do seu evento?"))

# Verifica se o número de participantes é válido
if num_participantes <= 0:
    print("Número inválido de participantes")
else:
    # Loop para coletar o nome dos amigos e atualizar o dicionário
    for amg in range(num_participantes):
        nome = input(f"Qual o nome do participante № {amg + 1}: ")
        item_dicionario = {nome: 0}
        amigos.update(item_dicionario)

    # Coleta o valor total da conta
    valor_conta = float(input("Qual o valor da conta total: R$"))

    # Pergunta se o usuário quer realizar um sorteio para isentar alguém do pagamento
    sorteio = input("Quer sortear alguém para ser isento do pagamento da conta?\n[S]/[N]:").upper()

    if sorteio == 'S':
        # Realiza o sorteio escolhendo uma pessoa aleatória do dicionário
        sortudo = random.choice(list(amigos.keys()))

        # Imprime o resultado do sorteio com uma pequena pausa
        print(f"Sorteando...")
        time.sleep(1.5)
        print('*' * 40)
        print(f"Sorteado(a): {sortudo}")
        print('*' * 40)

        # Atualiza os valores divididos no dicionário para todos, exceto o sorteado
        for nome in amigos:
            if nome == sortudo:
                continue
            else:
                amigos[nome] = valor_dividido_sorteio(valor_conta, amigos)

        # Imprime a lista de participantes com os valores atualizados
        print(f"Lista de participantes:")
        for c, v in amigos.items():
            print(f"Nome: {c} | Conta: R${v}")

    else:
        # Caso não haja sorteio, atualiza os valores divididos para todos normalmente
        print("Nenhum sorteio será realizado")
        for nome in amigos:
            amigos[nome] = valor_dividido_normal(valor_conta, amigos)

        # Imprime a lista de participantes com os valores atualizados
        print(f"Lista de participantes:")
        for c, v in amigos.items():
            print(f"Nome: {c} | Conta: R${v}")
