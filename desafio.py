menu = """
usuarios = {}
contas = {}

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

  # Função para cadastrar um usuário
def cadastrar_usuario(nome, cpf):
    if cpf in usuarios:
        print("Usuário já cadastrado.")
        return
    usuarios[cpf] = nome
    print(f"Usuário {nome} cadastrado com sucesso.")

# Função para cadastrar uma conta bancária
def cadastrar_conta(cpf, numero_conta):
    if numero_conta in contas:
        print("Número da conta já cadastrado.")
        return
    if cpf not in usuarios:
        print("Usuário não cadastrado.")
        return
    contas[numero_conta] = {
        'cpf': cpf,
        'saldo': 0
    }
    print(f"Conta número {numero_conta} cadastrada com sucesso.")

# Função para realizar um depósito
def depositar(numero_conta, valor):
    if numero_conta not in contas:
        print("Número da conta não encontrado.")
        return
    if valor <= 0:
        print("Valor de depósito deve ser positivo.")
        return
    contas[numero_conta]['saldo'] += valor
    print(f"Depósito de {valor} realizado com sucesso. Saldo atual: {contas[numero_conta]['saldo']}")

# Função para realizar um saque
def sacar(numero_conta, valor):
    if numero_conta not in contas:
        print("Número da conta não encontrado.")
        return
    if valor <= 0:
        print("Valor de saque deve ser positivo.")
        return
    if valor > contas[numero_conta]['saldo']:
        print("Saldo insuficiente para saque.")
        return
    contas[numero_conta]['saldo'] -= valor
    print(f"Saque de {valor} realizado com sucesso. Saldo atual: {contas[numero_conta]['saldo']}")

# Função para exibir o extrato
def extrato(numero_conta):
    if numero_conta not in contas:
        print("Número da conta não encontrado.")
        return
    saldo = contas[numero_conta]['saldo']
    print(f"Extrato da conta número {numero_conta}: Saldo atual: {saldo}")

# Testando as funções
cadastrar_usuario("João Silva", "12345678900")
cadastrar_usuario("Maria Oliveira", "09876543211")

cadastrar_conta("12345678900", "001")
cadastrar_conta("09876543211", "002")

depositar("001", 500)
sacar("001", 200)
extrato("001")

depositar("002", 1000)
sacar("002", 500)
extrato("002")
