import datetime

class ContaPoupanca(ContaBancaria):
    def __init__(self, nomeCliente, numConta, numAgencia, saldo, diaDeRendimento, taxaDeRendimento):
        super().__init__(nomeCliente, numConta, numAgencia, saldo)
        self.__diaDeRendimento = diaDeRendimento
        self.__taxaDeRendimento = taxaDeRendimento

    def getDiaDeRendimento(self):
        return self.__diaDeRendimento
    def setDiaDeRendimento(self, diaDeRendimento):
        self.__diaDeRendimento = diaDeRendimento

    def getTaxaDeRendimento(self):
        return self.__taxaDeRendimento
    def setTaxaDeRendimento(self, taxaDeRendimento):
        self.__taxaDeRendimento = taxaDeRendimento

    def calcularNovoSaldo(self):
        hoje = datetime.datetime.now().day
        if hoje == self.__diaDeRendimento:
            rendimento = self.getSaldo() * (self.__taxaDeRendimento / 100)
            self.setSaldo(self.getSaldo() + rendimento)
            return True
        return False

class ContaEspecial(ContaBancaria):
    def __init__(self, nomeCliente, numConta, numAgencia, saldo, limite):
        super().__init__(nomeCliente, numConta, numAgencia, saldo)
        self.__limite = limite

    def getLimite(self):
        return self.__limite
    def setLimite(self, limite):
        self.__limite = limite

    def sacar(self, valor):
        if self.getSaldo() + self.__limite >= valor and valor > 0:
            self.setSaldo(self.getSaldo() - valor)
            return self.getSaldo()
        else:
            return False

# Exemplo de uso
conta_poupanca = ContaPoupanca('Ana', '123456', 456, 1000, 15, 0.5)
conta_especial = ContaEspecial('Carlos', '654321', 789, 2000, 1000)

# Atualizar o saldo da conta poupança se for o dia de rendimento
conta_poupanca.calcularNovoSaldo()

# Sacar dinheiro da conta especial
conta_especial.sacar(300)

# Exibir informações das contas
print("Conta Poupança:")
print(conta_poupanca)

print("Conta Especial:")
print(conta_especial)
