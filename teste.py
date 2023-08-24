class ContaCorrente:
    def __init__(self, numero='', titular='', saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de {valor} realizado. Novo saldo: {self.saldo}"

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f"Saque de {valor} realizado. Novo saldo: {self.saldo}"
        else:
            return "Saldo insuficiente para saque."

# Instanciando um objeto da classe ContaCorrente
conta = ContaCorrente()

# Obtendo valores de entrada para as propriedades
conta.numero = input("Número da Conta: ")
conta.titular = input("Titular da Conta: ")
conta.saldo = float(input("Saldo Inicial: "))
123546
# Executando métodos e exibindo os resultados
valor_deposito = float(input("Valor do Depósito: "))
valor_saque = float(input("Valor do Saque: "))

resultado_deposito = conta.depositar(valor_deposito)
resultado_saque = conta.sacar(valor_saque)

print("\n=== Informações da Conta Corrente ===")
print("Número da Conta:", conta.numero)
print("Titular da Conta:", conta.titular)
print("Saldo Atual:", conta.saldo)
print("\n=== Resultados ===")
print(resultado_deposito)
print(resultado_saque)
